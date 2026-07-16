#!/usr/bin/env python3
"""Build the stable Phase 1 SQLite/JSONL interface from the enriched source DB."""
import argparse, json, random, sqlite3
from collections import Counter
from pathlib import Path

OPINION_TYPES={"010combined":"majority","020lead":"lead","030concurrence":"concurrence",
 "035concurrenceinpart":"concurrence","040dissent":"dissent","100trialcourt":"order",
 "070rehearing":"order","080onthemerits":"majority"}
CASE_TYPES={"tax":"tax","criminal":"criminal","civil_rights":"civil_rights","contract":"contract",
 "commercial":"commercial","property":"property","immigration":"immigration","labor_employment":"labor",
 "bankruptcy":"bankruptcy","administrative":"administrative","family":"family",
 "intellectual_property":"intellectual_property","tort":"other","civil":"other","government":"other","other":"other"}

def court_classification(court_id, name):
    """Return a coarse court type and a stable, queryable court level."""
    cid=(court_id or "").lower(); n=(name or "").lower()
    if "bankruptcy court" in n or "tax court" in n or "board of" in n or "commission" in n or "attorney general reports" in n:
        return "administrative", "administrative"
    if cid=="scotus" or "supreme court of the united states" in n:
        return "federal", "federal_supreme"
    if "court of appeals for the" in n or (cid.startswith("ca") and cid[2:].isdigit()) or "federal circuit" in n:
        return "federal", "federal_circuit"
    if "district court" in n and ("united states" in n or cid.endswith(("d","ed","wd","nd","sd"))):
        return "federal", "federal_district"
    # Appellate Division names contain "Supreme Court" but are intermediate
    # appellate courts, so this test must precede state supreme court matching.
    if "appellate division" in n or "court of appeal" in n or "court of appeals" in n or "appellate" in n or "commonwealth court" in n:
        return "state", "state_appellate"
    if "supreme court" in n:
        return "state", "state_supreme"
    if any(x in n for x in ("superior court","circuit court","county court","municipal court","family court","chancery court")):
        return "state", "state_trial"
    return "other", "other"

def load(value,default):
    try:return json.loads(value) if value else default
    except (json.JSONDecodeError,TypeError):return default

def schema(con):
    con.executescript("""
    PRAGMA foreign_keys=ON;
    CREATE TABLE cases(case_id TEXT PRIMARY KEY,cluster_id TEXT,docket_id TEXT,case_name TEXT,court_id TEXT,court_name TEXT,
      court_type TEXT,court_level TEXT,jurisdiction TEXT,date_filed TEXT,year_filed INTEGER,precedential_status TEXT,citation TEXT,
      absolute_url TEXT,full_text TEXT NOT NULL,source TEXT,raw_json TEXT,provenance_json TEXT);
    CREATE TABLE documents(document_id TEXT PRIMARY KEY,case_id TEXT NOT NULL,document_type TEXT,title TEXT,text TEXT NOT NULL,
      pdf_url TEXT,author TEXT,opinion_type TEXT,page_count INTEGER,source TEXT,raw_json TEXT,provenance_json TEXT,
      FOREIGN KEY(case_id) REFERENCES cases(case_id));
    CREATE TABLE docket_entries(entry_id TEXT PRIMARY KEY,case_id TEXT,date TEXT,entry_number TEXT,description TEXT,
      document_ids TEXT,source TEXT,raw_json TEXT,FOREIGN KEY(case_id) REFERENCES cases(case_id));
    CREATE TABLE case_features(case_id TEXT PRIMARY KEY,case_type_weak TEXT,procedural_stage_current TEXT,
      procedural_stage_history TEXT,outcome_keyword TEXT,classification_evidence TEXT,
      FOREIGN KEY(case_id) REFERENCES cases(case_id));
    CREATE INDEX idx_cases_court ON cases(court_id); CREATE INDEX idx_cases_year ON cases(year_filed);
    CREATE INDEX idx_cases_constraints ON cases(court_type,court_level,year_filed);
    CREATE INDEX idx_docs_case ON documents(case_id); CREATE INDEX idx_features_type ON case_features(case_type_weak);
    """)

def main():
    p=argparse.ArgumentParser();p.add_argument("--source-db",required=True);p.add_argument("--output-dir",required=True)
    p.add_argument("--min-text-chars",type=int,default=350);p.add_argument("--seed",type=int,default=20260709);a=p.parse_args()
    out=Path(a.output_dir);out.mkdir(parents=True,exist_ok=True);db=out/"legal_cases.db"
    if db.exists():db.unlink()
    src=sqlite3.connect(f"file:{Path(a.source_db).resolve()}?mode=ro",uri=True);src.row_factory=sqlite3.Row
    dst=sqlite3.connect(db);schema(dst);kept=set();case_rows=[];feature_rows=[]
    for r in src.execute("SELECT c.*,lc.classification_json,f.analysis_evidence FROM cases c JOIN legal_categories lc USING(case_id) JOIN case_features f USING(case_id) ORDER BY c.case_id"):
        text=r["full_text"] or ""
        if len(text)<a.min_text_chars:continue
        classification=load(r["classification_json"],{});domains=classification.get("legal_domain",[])
        types=[]
        for domain in domains:
            value=CASE_TYPES.get(domain,"other")
            if value not in types:types.append(value)
        if not types:types=["other"]
        types=types[:2];stage=classification.get("procedural_stage",{});outcomes=classification.get("outcome",[])
        court_type, level=court_classification(r["court_id"],r["court_name"]);case=(r["case_id"],r["cluster_id"],r["docket_id"],r["case_name"],
          r["court_id"],r["court_name"],court_type,level,"US",r["date_filed"],r["year_filed"],r["precedential_status"],r["citation"],
          r["absolute_url"],text,r["source"],r["raw_json"],r["provenance_json"])
        dst.execute("INSERT INTO cases VALUES("+",".join("?"*18)+")",case);kept.add(r["case_id"])
        case_rows.append(dict(zip(["case_id","cluster_id","docket_id","case_name","court_id","court_name","court_type","court_level","jurisdiction","date_filed","year_filed","precedential_status","citation","absolute_url","full_text","source","raw_json","provenance_json"],case)))
        feature=(r["case_id"],json.dumps(types),stage.get("current","decision"),json.dumps(stage.get("history",[])),json.dumps(outcomes),r["analysis_evidence"] or "[]")
        dst.execute("INSERT INTO case_features VALUES(?,?,?,?,?,?)",feature);feature_rows.append(dict(zip(["case_id","case_type_weak","procedural_stage_current","procedural_stage_history","outcome_keyword","classification_evidence"],feature)))
    doc_rows=[]
    for r in src.execute("SELECT * FROM documents ORDER BY document_id"):
        if r["case_id"] not in kept or len(r["text"] or "")<a.min_text_chars:continue
        opinion_type=OPINION_TYPES.get((r["opinion_type"] or "").lower(),"unknown")
        row=(r["document_id"],r["case_id"],r["document_type"],r["title"],r["text"],r["pdf_url"],r["author"],opinion_type,r["page_count"],r["source"],r["raw_json"],r["provenance_json"])
        dst.execute("INSERT INTO documents VALUES("+",".join("?"*12)+")",row);doc_rows.append(dict(zip(["document_id","case_id","document_type","title","text","pdf_url","author","opinion_type","page_count","source","raw_json","provenance_json"],row)))
    docket_rows=[]
    for r in src.execute("SELECT * FROM docket_entries ORDER BY entry_id"):
        if r["case_id"] not in kept:continue
        row=(r["entry_id"],r["case_id"],r["date"],r["entry_number"],r["description"],r["document_ids"],r["source"],r["raw_json"])
        dst.execute("INSERT INTO docket_entries VALUES(?,?,?,?,?,?,?,?)",row);docket_rows.append(dict(zip(["entry_id","case_id","date","entry_number","description","document_ids","source","raw_json"],row)))
    dst.commit();dst.close();src.close()
    for name,rows in (("cases.jsonl",case_rows),("documents.jsonl",doc_rows),("case_features.jsonl",feature_rows)):
        with (out/name).open("w") as f:
            for row in rows:f.write(json.dumps(row,ensure_ascii=False)+"\n")
    con=sqlite3.connect(db);con.row_factory=sqlite3.Row
    quality={"total_cases":len(case_rows),"missing_full_text":sum(not x["full_text"] for x in case_rows),
      "missing_court":sum(not x["court_name"] for x in case_rows),"missing_date":sum(not x["date_filed"] for x in case_rows),
      "missing_case_name":sum(not x["case_name"] for x in case_rows),"type_distribution":dict(Counter(t for x in feature_rows for t in load(x["case_type_weak"],[]))),
      "court_distribution":dict(Counter(x["court_name"] or "unknown" for x in case_rows).most_common()),
      "court_type_distribution":dict(Counter(x["court_type"] for x in case_rows)),
      "court_level_distribution":dict(Counter(x["court_level"] for x in case_rows)),
      "year_distribution":dict(sorted(Counter(str(x["year_filed"]) for x in case_rows).items()))}
    (out/"dataset_quality_report.json").write_text(json.dumps(quality,indent=2)+"\n")
    random_rows=random.Random(a.seed).sample(case_rows,min(20,len(case_rows)))
    validation={"field_completeness":{key:round(sum(bool(x.get(key)) for x in case_rows)/len(case_rows),4) for key in ("case_id","case_name","court_name","court_type","court_level","date_filed","year_filed","full_text","jurisdiction")},
      "classification_distribution":quality["type_distribution"],"random_20_cases":[{k:x[k] for k in ("case_id","case_name","court_name","court_type","court_level","date_filed","year_filed")} for x in random_rows]}
    (out/"phase1_validation_report.json").write_text(json.dumps(validation,indent=2)+"\n")
    print(json.dumps({"output":str(out),"cases":len(case_rows),"documents":len(doc_rows),"docket_entries":len(docket_rows)},indent=2))
if __name__=="__main__":main()
