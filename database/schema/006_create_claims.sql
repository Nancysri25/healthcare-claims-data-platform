CREATE TABLE IF NOT EXISTS claims (

    claim_id SERIAL PRIMARY KEY,

    claim_number VARCHAR(30) UNIQUE NOT NULL,

    member_id INT NOT NULL,

    provider_id INT NOT NULL,

    diagnosis_code_id INT NOT NULL,

    procedure_code_id INT NOT NULL,

    claim_date DATE NOT NULL,

    service_date DATE NOT NULL,

    billed_amount DECIMAL(12,2),

    approved_amount DECIMAL(12,2),

    patient_responsibility DECIMAL(12,2),

    claim_status VARCHAR(30),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_member
        FOREIGN KEY(member_id)
        REFERENCES members(member_id),

    CONSTRAINT fk_provider
        FOREIGN KEY(provider_id)
        REFERENCES providers(provider_id),

    CONSTRAINT fk_diagnosis
        FOREIGN KEY(diagnosis_code_id)
        REFERENCES diagnosis_codes(diagnosis_code_id),

    CONSTRAINT fk_procedure
        FOREIGN KEY(procedure_code_id)
        REFERENCES procedure_codes(procedure_code_id)
);