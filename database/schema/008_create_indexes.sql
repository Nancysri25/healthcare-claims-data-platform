CREATE INDEX idx_member_number
ON members(member_number);

CREATE INDEX idx_claim_number
ON claims(claim_number);

CREATE INDEX idx_claim_date
ON claims(claim_date);

CREATE INDEX idx_provider_name
ON providers(provider_name);

CREATE INDEX idx_icd10
ON diagnosis_codes(icd10_code);

CREATE INDEX idx_cpt
ON procedure_codes(cpt_code);