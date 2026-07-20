CREATE TABLE IF NOT EXISTS insurance_plans (
    insurance_plan_id SERIAL PRIMARY KEY,
    plan_name VARCHAR(100) NOT NULL,
    plan_type VARCHAR(50),
    coverage_percentage DECIMAL(5,2),
    deductible DECIMAL(10,2),
    out_of_pocket_max DECIMAL(10,2),
    monthly_premium DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);