CREATE TABLE dim_court (
        court_id TEXT PRIMARY KEY, court_name TEXT, court_name_short TEXT,
        jurisdiction_raw TEXT, jurisdiction_type TEXT NOT NULL, court_level TEXT NOT NULL,
        circuit TEXT, state_code TEXT, is_active INTEGER, start_date TEXT, end_date TEXT,
        raw_json TEXT, provenance_json TEXT
    );
CREATE TABLE case_record (
        case_id TEXT PRIMARY KEY, cluster_id TEXT UNIQUE NOT NULL, docket_id TEXT, court_id TEXT,
        case_name TEXT, case_name_docket TEXT, docket_number TEXT, decision_date TEXT, decision_year INTEGER,
        citations_json TEXT NOT NULL, publication_status_raw TEXT, precedential_status TEXT NOT NULL,
        source TEXT, judges_raw TEXT, syllabus TEXT, posture TEXT, procedural_history TEXT,
        jurisdiction_type TEXT, court_level TEXT, opinion_ids_json TEXT NOT NULL,
        raw_json TEXT, provenance_json TEXT,
        FOREIGN KEY(court_id) REFERENCES dim_court(court_id)
    );
CREATE TABLE opinion_record (
        opinion_id TEXT PRIMARY KEY, cluster_id TEXT NOT NULL, opinion_type_raw TEXT,
        opinion_type TEXT NOT NULL, opinion_group TEXT NOT NULL, author_id TEXT, per_curiam INTEGER,
        html_with_citations TEXT, plain_text TEXT, preferred_text TEXT, preferred_text_source TEXT,
        text_length INTEGER NOT NULL, text_sha1 TEXT, cited_opinion_ids_json TEXT NOT NULL,
        has_usable_text INTEGER NOT NULL, quality_metrics_json TEXT NOT NULL, raw_json TEXT, provenance_json TEXT,
        FOREIGN KEY(cluster_id) REFERENCES case_record(cluster_id)
    );
CREATE TABLE case_features (
        case_id TEXT PRIMARY KEY, practice_area_json TEXT NOT NULL, primary_topic TEXT,
        secondary_topics_json TEXT NOT NULL, statutes_json TEXT NOT NULL,
        constitutional_provisions_json TEXT NOT NULL, disposition_json TEXT NOT NULL,
        primary_legal_issue TEXT, holding TEXT, relief_ordered_json TEXT NOT NULL,
        government_authority_direction TEXT, feature_source_json TEXT NOT NULL,
        confidence_json TEXT NOT NULL, evidence_spans_json TEXT NOT NULL, rule_signals_json TEXT NOT NULL,
        FOREIGN KEY(case_id) REFERENCES case_record(case_id)
    );
CREATE TABLE search_document (
        document_id TEXT PRIMARY KEY, case_id TEXT NOT NULL, opinion_id TEXT NOT NULL, cluster_id TEXT NOT NULL,
        case_name TEXT, court_id TEXT, court_level TEXT, jurisdiction_type TEXT,
        decision_date TEXT, decision_year INTEGER, precedential_status TEXT,
        opinion_type TEXT, section_type TEXT NOT NULL, section_weight REAL NOT NULL,
        primary_topic TEXT, statutes_json TEXT NOT NULL, chunk_index INTEGER NOT NULL,
        chunk_text TEXT NOT NULL, chunk_token_count INTEGER NOT NULL, bm25_text TEXT NOT NULL,
        embedding_json TEXT NOT NULL DEFAULT '[]',
        FOREIGN KEY(case_id) REFERENCES case_record(case_id),
        FOREIGN KEY(opinion_id) REFERENCES opinion_record(opinion_id)
    );
CREATE TABLE build_state (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE INDEX idx_dim_court_jurisdiction_level ON dim_court(jurisdiction_type, court_level);
CREATE INDEX idx_dim_court_circuit ON dim_court(circuit);
CREATE INDEX idx_dim_court_state ON dim_court(state_code);
CREATE INDEX idx_case_cluster ON case_record(cluster_id);
CREATE INDEX idx_case_docket ON case_record(docket_id);
CREATE INDEX idx_case_court ON case_record(court_id);
CREATE INDEX idx_case_date ON case_record(decision_date, decision_year);
CREATE INDEX idx_case_status ON case_record(precedential_status);
CREATE INDEX idx_case_jurisdiction_level ON case_record(jurisdiction_type, court_level);
CREATE INDEX idx_opinion_cluster ON opinion_record(cluster_id);
CREATE INDEX idx_opinion_group ON opinion_record(opinion_group, has_usable_text);
CREATE INDEX idx_opinion_sha1 ON opinion_record(text_sha1);
CREATE INDEX idx_search_case ON search_document(case_id);
CREATE INDEX idx_search_opinion ON search_document(opinion_id);
CREATE INDEX idx_search_metadata ON search_document(court_level, decision_year, section_type);
CREATE TABLE annotation_release (
    release_id TEXT PRIMARY KEY,
    taxonomy_version TEXT NOT NULL,
    feature_version TEXT NOT NULL,
    created_at TEXT NOT NULL,
    taxonomy_record_count INTEGER NOT NULL,
    feature_job_count INTEGER NOT NULL,
    metadata_json TEXT NOT NULL
);
CREATE TABLE case_taxonomy_v3 (
    case_id TEXT PRIMARY KEY,
    annotation_status TEXT NOT NULL,
    primary_practice_area TEXT,
    secondary_practice_areas_json TEXT NOT NULL,
    matter_types_json TEXT NOT NULL,
    legal_issues_json TEXT NOT NULL,
    unmapped_matter_types_json TEXT NOT NULL,
    unmapped_legal_issues_json TEXT NOT NULL,
    needs_review INTEGER NOT NULL,
    review_applied INTEGER NOT NULL,
    review_status TEXT,
    raw_annotation_json TEXT NOT NULL,
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);
CREATE TABLE case_practice_area_v3 (
    case_id TEXT NOT NULL,
    practice_area TEXT NOT NULL,
    area_role TEXT NOT NULL,
    confidence REAL,
    evidence_json TEXT NOT NULL,
    PRIMARY KEY(case_id, practice_area, area_role),
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);
CREATE TABLE case_matter_type_v3 (
    case_id TEXT NOT NULL,
    matter_type TEXT NOT NULL,
    practice_area TEXT,
    confidence REAL,
    needs_review INTEGER NOT NULL,
    evidence_json TEXT NOT NULL,
    PRIMARY KEY(case_id, matter_type),
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);
CREATE TABLE case_legal_issue_v3 (
    case_id TEXT NOT NULL,
    issue_id TEXT NOT NULL,
    issue_status TEXT,
    mention_confidence REAL,
    adjudication_confidence REAL,
    evidence_json TEXT NOT NULL,
    PRIMARY KEY(case_id, issue_id),
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);
CREATE TABLE matter_type_feature_job_v1_1 (
    job_id TEXT PRIMARY KEY,
    case_id TEXT NOT NULL,
    case_name TEXT,
    annotation_source TEXT,
    annotation_status TEXT NOT NULL,
    review_history_json TEXT NOT NULL,
    human_review_json TEXT,
    raw_annotation_json TEXT NOT NULL,
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);
CREATE TABLE matter_type_annotation_v1_1 (
    job_id TEXT NOT NULL,
    case_id TEXT NOT NULL,
    matter_type TEXT NOT NULL,
    matter_occurrence INTEGER NOT NULL,
    matter_status TEXT,
    matter_target_json TEXT NOT NULL,
    PRIMARY KEY(job_id, matter_type, matter_occurrence),
    FOREIGN KEY(job_id) REFERENCES matter_type_feature_job_v1_1(job_id),
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);
CREATE TABLE matter_type_feature_value_v1_1 (
    job_id TEXT NOT NULL,
    case_id TEXT NOT NULL,
    matter_type TEXT NOT NULL,
    matter_occurrence INTEGER NOT NULL,
    feature_key TEXT NOT NULL,
    feature_occurrence INTEGER NOT NULL,
    value_status TEXT NOT NULL,
    value_json TEXT,
    value_text TEXT,
    value_number REAL,
    unit TEXT,
    confidence REAL,
    missing_reason TEXT,
    evidence_json TEXT NOT NULL,
    PRIMARY KEY(job_id, matter_type, matter_occurrence, feature_key, feature_occurrence),
    FOREIGN KEY(job_id) REFERENCES matter_type_feature_job_v1_1(job_id),
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);
CREATE TABLE annotation_registry_snapshot (
    registry_name TEXT PRIMARY KEY,
    registry_version TEXT,
    sha256 TEXT NOT NULL,
    content_json TEXT NOT NULL
);
CREATE INDEX idx_taxonomy_v3_practice ON case_taxonomy_v3(primary_practice_area, needs_review);
CREATE INDEX idx_practice_area_v3 ON case_practice_area_v3(practice_area, area_role, case_id);
CREATE INDEX idx_matter_type_v3 ON case_matter_type_v3(matter_type, needs_review, case_id);
CREATE INDEX idx_legal_issue_v3 ON case_legal_issue_v3(issue_id, issue_status, case_id);
CREATE INDEX idx_feature_job_case ON matter_type_feature_job_v1_1(case_id, annotation_status);
CREATE INDEX idx_feature_annotation_type ON matter_type_annotation_v1_1(matter_type, case_id);
CREATE INDEX idx_feature_value_key_status ON matter_type_feature_value_v1_1(feature_key, value_status, case_id);
CREATE INDEX idx_feature_value_numeric ON matter_type_feature_value_v1_1(feature_key, value_number, case_id)
    WHERE value_number IS NOT NULL;
CREATE INDEX idx_feature_value_text ON matter_type_feature_value_v1_1(feature_key, value_text, case_id)
    WHERE value_text IS NOT NULL;
CREATE TABLE sqlite_stat1(tbl,idx,stat);
CREATE TABLE sqlite_stat4(tbl,idx,neq,nlt,ndlt,sample);
