CREATE TABLE IF NOT EXISTS providers (
    provider_id SERIAL PRIMARY KEY,
    provider_name VARCHAR(255) NOT NULL,
    provider_type VARCHAR(100),
    npi_number VARCHAR(20) UNIQUE,
    city VARCHAR(100),
    state VARCHAR(50),
    phone_number VARCHAR(30),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);