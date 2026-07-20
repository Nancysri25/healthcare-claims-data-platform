import random
import pandas as pd

from etl.utils.config import RAW_DATA, NUM_PROCEDURE_CODES
from etl.utils.logger import logger

procedure_pool = [
    ("99213", "Office Visit"),
    ("93000", "ECG"),
    ("80053", "Comprehensive Metabolic Panel"),
    ("70450", "CT Scan"),
    ("71046", "Chest X-Ray"),
    ("85025", "Complete Blood Count"),
    ("36415", "Blood Collection"),
    ("81001", "Urinalysis")
]

procedures = []

for i in range(NUM_PROCEDURE_CODES):
    code, desc = random.choice(procedure_pool)

    procedures.append({
        "procedure_code_id": i + 1,
        "cpt_code": f"{code}_{i+1}",
        "procedure_description": desc,
        "procedure_category": desc.split()[0],
        "average_cost": random.randint(50, 3000)
    })

df = pd.DataFrame(procedures)

output_file = RAW_DATA / "procedure_codes.csv"

df.to_csv(output_file, index=False)

logger.info(f"Generated {len(df)} procedure codes")