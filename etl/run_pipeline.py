from pathlib import Path

from etl.loading.load_csv import load_csv

raw = Path("data/raw")
processed = Path("data/processed")

load_csv(
    raw / "insurance_plans.csv",
    "insurance_plans",
    "insurance_plan_id"
)

load_csv(
    raw / "members.csv",
    "members",
    "member_id"
)

load_csv(
    raw / "providers.csv",
    "providers",
    "provider_id"
)

load_csv(
    raw / "diagnosis_codes.csv",
    "diagnosis_codes",
    "diagnosis_code_id"
)

load_csv(
    raw / "procedure_codes.csv",
    "procedure_codes",
    "procedure_code_id"
)

# Load the transformed claims file
load_csv(
    processed / "claims_transformed.csv",
    "claims",
    "claim_number"
)