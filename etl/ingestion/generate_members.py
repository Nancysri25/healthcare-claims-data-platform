import random
from faker import Faker
import pandas as pd

from etl.utils.config import RAW_DATA, NUM_MEMBERS, NUM_INSURANCE_PLANS
from etl.utils.logger import logger

fake = Faker("en_US")

members = []

for i in range(1, NUM_MEMBERS + 1):

    members.append(
        {
            "member_number": f"MBR{i:08}",
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "gender": random.choice(["Male", "Female"]),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=90),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "zip_code": fake.zipcode(),
            "insurance_plan_id": random.randint(1, NUM_INSURANCE_PLANS),
        }
    )

df = pd.DataFrame(members)

output_file = RAW_DATA / "members.csv"

df.to_csv(output_file, index=False)

logger.info(f"Generated {len(df)} members")
logger.info(f"Saved to {output_file}")