CREATE TABLE IF NOT EXISTS claims (

    claim_id SERIAL PRIMARY KEY,

    -- Claim identifiers
    claim_number VARCHAR(50) UNIQUE NOT NULL,

    -- Foreign keys
    member_id INT NOT NULL,
    provider_id INT NOT NULL,
    diagnosis_code_id INT,
    procedure_code_id INT,

    -- Claim details
    claim_type VARCHAR(50),
    place_of_service VARCHAR(100),
    payer_name VARCHAR(100),

    -- Dates
    service_date DATE,
    admission_date DATE,
    discharge_date DATE,
    claim_date DATE,
    processing_date DATE,

    -- Financial details
    billed_amount NUMERIC(12,2),
    approved_amount NUMERIC(12,2),
    patient_responsibility NUMERIC(12,2),

    -- Claim status
    claim_status VARCHAR(50),

    -- Transformed fields
    processing_days INT,
    approval_percentage NUMERIC(5,2),
    claim_month VARCHAR(7),
    claim_year INT,
    length_of_stay INT,

    -- Audit columns
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Foreign key constraints
    CONSTRAINT fk_member
        FOREIGN KEY(member_id)
        REFERENCES members(member_id),

    CONSTRAINT fk_provider
        FOREIGN KEY(provider_id)
        REFERENCES providers(provider_id),

    CONSTRAINT fk_diagnosis_code
        FOREIGN KEY(diagnosis_code_id)
        REFERENCES diagnosis_codes(diagnosis_code_id),

    CONSTRAINT fk_procedure_code
        FOREIGN KEY(procedure_code_id)
        REFERENCES procedure_codes(procedure_code_id)

);