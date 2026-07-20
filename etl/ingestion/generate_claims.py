import random
from datetime import datetime, timedelta

import pandas as pd

from etl.utils.config import RAW_DATA, NUM_CLAIMS
from etl.utils.file_utils import read_csv, write_csv
from etl.utils.logger import logger

# Read master data
members = read_csv(RAW_DATA / "members.csv")
providers = read_csv(RAW_DATA / "providers.csv")
diagnosis_codes = read_csv(RAW_DATA / "diagnosis_codes.csv")
procedure_codes = read_csv(RAW_DATA / "procedure_codes.csv")
insurance_plans = read_csv(RAW_DATA / "insurance_plans.csv")

coverage_lookup = dict(
    zip(
        insurance_plans["insurance_plan_id"],
        insurance_plans["coverage_percentage"]
    )
)

claims = []

claim_types = [
    "Inpatient",
    "Outpatient",
    "Emergency",
    "Pharmacy"
]

claim_statuses = [
    "Approved",
    "Denied",
    "Pending"
]

payer_names = [
    "Aetna",
    "UnitedHealthcare",
    "Cigna",
    "Blue Cross Blue Shield",
    "Humana"
]

place_of_service = [
    "Hospital",
    "Clinic",
    "Emergency Room",
    "Laboratory",
    "Pharmacy"
]

today = datetime.today()


for i in range(1, NUM_CLAIMS + 1):

    member = members.sample(1).iloc[0]
    provider = providers.sample(1).iloc[0]
    diagnosis = diagnosis_codes.sample(1).iloc[0]
    procedure = procedure_codes.sample(1).iloc[0]

    # Get coverage from the member's insurance plan
    coverage = coverage_lookup[member["insurance_plan_id"]]

    claim_type = random.choice(claim_types)

    service_date = today - timedelta(days=random.randint(0, 730))
    claim_date = service_date + timedelta(days=random.randint(0, 5))
    processing_date = claim_date + timedelta(days=random.randint(1, 10))

    # Base billed amount from procedure average cost
    billed_amount = float(procedure["average_cost"])

    # Add some variation (+/-20%)
    billed_amount *= random.uniform(0.8, 1.2)
    billed_amount = round(billed_amount, 2)

    approved_amount = round(
        billed_amount * (coverage / 100),
        2
    )

    patient_responsibility = round(
        billed_amount - approved_amount,
        2
    )

    if approved_amount == billed_amount:
        status = "Approved"
    elif approved_amount < billed_amount * 0.5:
        status = "Denied"
    else:
        status = random.choice(["Approved", "Pending"])

    admission_date = None
    discharge_date = None

    if claim_type == "Inpatient":
        admission_date = service_date
        discharge_date = admission_date + timedelta(
            days=random.randint(1, 7)
        )

    claims.append({

        "claim_number": f"CLM{i:08}",

        "member_id": member["member_id"],

        "provider_id": provider["provider_id"],

        "diagnosis_code_id": diagnosis["diagnosis_code_id"],

        "procedure_code_id": procedure["procedure_code_id"],

        "claim_type": claim_type,

        "place_of_service": random.choice(place_of_service),

        "payer_name": random.choice(payer_names),

        "service_date": service_date.date(),

        "admission_date": admission_date.date() if admission_date else None,

        "discharge_date": discharge_date.date() if discharge_date else None,

        "claim_date": claim_date.date(),

        "processing_date": processing_date.date(),

        "billed_amount": billed_amount,

        "approved_amount": approved_amount,

        "patient_responsibility": patient_responsibility,

        "claim_status": status

    })

df = pd.DataFrame(claims)

write_csv(df, RAW_DATA / "claims.csv")

logger.info(f"Generated {len(df)} claims")