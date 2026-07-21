import time

import pandas as pd
from sqlalchemy import text

from etl.loading.database_connection import engine
from etl.loading.upsert import postgres_upsert
from etl.utils.logger import logger


def load_csv(file_path, table_name, primary_key):

    start = time.time()

    df = pd.read_csv(file_path)

    staging_table = f"{table_name}_staging"

    with engine.begin() as conn:

        # Remove old staging table
        conn.execute(text(f"DROP TABLE IF EXISTS {staging_table};"))

        # Create staging table with SAME schema as target
        conn.execute(
    text(
        f"""
        CREATE TABLE {staging_table}
        (
            LIKE {table_name}
            INCLUDING DEFAULTS
            INCLUDING GENERATED
            INCLUDING IDENTITY
        );
        """
    )
)

    # Load into staging
    df.to_sql(
        staging_table,
        engine,
        if_exists="append",
        index=False,
        chunksize=5000,
        method="multi",
    )

    postgres_upsert(table_name, primary_key)

    # Cleanup
    with engine.begin() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {staging_table};"))

    end = time.time()

    logger.info(f"{len(df)} rows loaded into {table_name}")
    logger.info(f"Execution Time : {round(end-start,2)} seconds")