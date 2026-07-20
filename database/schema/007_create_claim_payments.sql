CREATE TABLE IF NOT EXISTS claim_payments (

    payment_id SERIAL PRIMARY KEY,

    claim_id INT NOT NULL,

    payment_date DATE,

    payment_amount DECIMAL(12,2),

    payment_method VARCHAR(50),

    payment_status VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_claim
        FOREIGN KEY(claim_id)
        REFERENCES claims(claim_id)
);