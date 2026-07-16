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
CREATE INDEX idx_cases_court ON cases(court_id);
CREATE INDEX idx_cases_year ON cases(year_filed);
CREATE INDEX idx_cases_constraints ON cases(court_type,court_level,year_filed);
CREATE INDEX idx_docs_case ON documents(case_id);
CREATE INDEX idx_features_type ON case_features(case_type_weak);
