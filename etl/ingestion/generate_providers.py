import random
from faker import Faker
import pandas as pd

from etl.utils.config import RAW_DATA, NUM_PROVIDERS
from etl.utils.logger import logger

fake = Faker("en_US")

provider_types = [
    "Hospital",
    "Clinic",
    "Primary Care",
    "Specialist",
    "Laboratory",
    "Pharmacy",
    "Urgent Care"
]

providers = []

for i in range(1, NUM_PROVIDERS + 1):

    providers.append(
        {
            "provider_id": i,
            "provider_name": fake.company() + " Medical Center",
            "provider_type": random.choice(provider_types),
            "npi_number": str(fake.random_number(digits=10, fix_len=True)),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "phone_number": fake.phone_number()
        }
    )

df = pd.DataFrame(providers)

output_file = RAW_DATA / "providers.csv"

df.to_csv(output_file, index=False)

logger.info(f"Generated {len(df)} providers")
logger.info(f"Saved to {output_file}")