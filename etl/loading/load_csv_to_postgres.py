import pandas as pd

from etl.loading.database_connection import engine
from etl.utils.logger import logger


def load_csv(file_path, table_name):
    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    logger.info(f"Loaded {len(df)} rows into {table_name}")

#gives us one reusable function that can load any CSV into PostgreSQL.