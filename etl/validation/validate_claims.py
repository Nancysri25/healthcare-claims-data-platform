import pandas as pd

from etl.utils.config import RAW_DATA
from etl.utils.file_utils import read_csv, write_csv
from etl.utils.logger import logger

claims = read_csv(RAW_DATA / "claims.csv")

logger.info(f"Original Records : {len(claims)}")

# Remove duplicate claim numbers
claims = claims.drop_duplicates(subset=["claim_number"])

# Remove rows with missing foreign keys
claims = claims.dropna(
    subset=[
        "member_id",
        "provider_id",
        "diagnosis_code_id",
        "procedure_code_id"
    ]
)

# Approved amount cannot exceed billed amount
claims = claims[
    claims["approved_amount"] <= claims["billed_amount"]
]

logger.info(f"Valid Records : {len(claims)}")

write_csv(
    claims,
    RAW_DATA.parent / "processed" / "claims_validated.csv"
)

logger.info("Validation Complete")