import pandas as pd

from etl.utils.config import RAW_DATA
from etl.utils.file_utils import read_csv, write_csv
from etl.utils.logger import logger

claims = read_csv(RAW_DATA.parent / "processed" / "claims_validated.csv")

logger.info(f"Loaded {len(claims)} validated claims")

# Claim processing time
claims["processing_days"] = (
    pd.to_datetime(claims["processing_date"])
    - pd.to_datetime(claims["claim_date"])
).dt.days

# Approval percentage
claims["approval_percentage"] = (
    claims["approved_amount"] / claims["billed_amount"] * 100
).round(2)

# Claim month
claims["claim_month"] = pd.to_datetime(
    claims["claim_date"]
).dt.to_period("M").astype(str)

# Claim year
claims["claim_year"] = pd.to_datetime(
    claims["claim_date"]
).dt.year

#hospital stay calc
claims["length_of_stay"] = (
    pd.to_datetime(claims["discharge_date"])
    - pd.to_datetime(claims["admission_date"])
).dt.days

claims["length_of_stay"] = (
    claims["length_of_stay"]
    .fillna(0)
    .astype(int)
)

#saving the transformed data
write_csv(
    claims,
    RAW_DATA.parent / "processed" / "claims_transformed.csv"
)

logger.info("Transformation Complete")