CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    gender VARCHAR(10),
    date_of_birth DATE,
    state VARCHAR(50),
    insurance_plan VARCHAR(100)
);

CREATE TABLE providers (
    provider_id SERIAL PRIMARY KEY,
    provider_name VARCHAR(255),
    provider_type VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(50)
);