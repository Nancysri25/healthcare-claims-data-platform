from pathlib import Path

from etl.loading.load_csv import load_csv

raw = Path("data/raw")
processed = Path("data/processed")

load_csv(raw / "insurance_plans.csv", "insurance_plans")
load_csv(raw / "members.csv", "members")
load_csv(raw / "providers.csv", "providers")
load_csv(raw / "diagnosis_codes.csv", "diagnosis_codes")
load_csv(raw / "procedure_codes.csv", "procedure_codes")

load_csv(
    processed / "claims_transformed.csv",
    "claims"
)