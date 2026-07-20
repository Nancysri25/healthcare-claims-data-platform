CREATE TABLE IF NOT EXISTS procedure_codes (
    procedure_code_id SERIAL PRIMARY KEY,
    cpt_code VARCHAR(10) UNIQUE NOT NULL,
    procedure_description VARCHAR(255),
    procedure_category VARCHAR(100),
    average_cost DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);