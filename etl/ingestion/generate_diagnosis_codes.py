import random
import pandas as pd

from etl.utils.config import RAW_DATA, NUM_DIAGNOSIS_CODES
from etl.utils.logger import logger

diagnosis_pool = [
    ("E11.9", "Type 2 Diabetes"),
    ("I10", "Hypertension"),
    ("J45.909", "Asthma"),
    ("M54.5", "Low Back Pain"),
    ("E78.5", "Hyperlipidemia"),
    ("F41.1", "Anxiety Disorder"),
    ("K21.9", "GERD"),
    ("N39.0", "Urinary Tract Infection"),
    ("J06.9", "Upper Respiratory Infection"),
    ("R51", "Headache")
]

diagnoses = []

for i in range(NUM_DIAGNOSIS_CODES):
    code, desc = random.choice(diagnosis_pool)

    diagnoses.append({
        "icd10_code": f"{code}_{i+1}",
        "diagnosis_description": desc,
        "diagnosis_category": desc.split()[0],
        "chronic_condition": random.choice([True, False])
    })

df = pd.DataFrame(diagnoses)

output_file = RAW_DATA / "diagnosis_codes.csv"

df.to_csv(output_file, index=False)

logger.info(f"Generated {len(df)} diagnosis codes")