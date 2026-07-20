import random
import pandas as pd

from etl.utils.config import RAW_DATA, NUM_INSURANCE_PLANS
from etl.utils.logger import logger

PLAN_TYPES = {
    "Bronze": 60,
    "Silver": 70,
    "Gold": 80,
    "Platinum": 90
}

plans = []

for i in range(1, NUM_INSURANCE_PLANS + 1):
    plan_type = random.choice(list(PLAN_TYPES.keys()))

    plans.append({
        "insurance_plan_id": i,
        "plan_name": f"{plan_type} Plan {i}",
        "plan_type": plan_type,
        "coverage_percentage": PLAN_TYPES[plan_type],
        "deductible": random.randint(1000, 8000),
        "out_of_pocket_max": random.randint(5000, 12000),
        "monthly_premium": random.randint(250, 900)
    })

df = pd.DataFrame(plans)

output_path = RAW_DATA / "insurance_plans.csv"

df.to_csv(output_path, index=False)

logger.info(f"Generated {len(df)} insurance plans")
logger.info(f"Saved file to {output_path}")