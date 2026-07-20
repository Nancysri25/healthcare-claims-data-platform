CREATE TABLE IF NOT EXISTS members (
    member_id SERIAL PRIMARY KEY,
    member_number VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    date_of_birth DATE,
    phone_number VARCHAR(30),
    email VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    insurance_plan_id INT REFERENCES insurance_plans(insurance_plan_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);