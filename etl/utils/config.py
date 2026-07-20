from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"
REJECTED_DATA = PROJECT_ROOT / "data" / "rejected"

RAW_DATA.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA.mkdir(parents=True, exist_ok=True)
REJECTED_DATA.mkdir(parents=True, exist_ok=True)

NUM_INSURANCE_PLANS = 100
NUM_MEMBERS = 10000
NUM_PROVIDERS = 2000
NUM_DIAGNOSIS_CODES = 250
NUM_PROCEDURE_CODES = 250
NUM_CLAIMS = 100000