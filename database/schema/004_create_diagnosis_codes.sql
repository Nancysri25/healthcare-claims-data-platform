CREATE TABLE IF NOT EXISTS diagnosis_codes (
    diagnosis_code_id SERIAL PRIMARY KEY,
    icd10_code VARCHAR(10) UNIQUE NOT NULL,
    diagnosis_description VARCHAR(255) NOT NULL,
    diagnosis_category VARCHAR(100),
    chronic_condition BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);