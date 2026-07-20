import time

import pandas as pd

from etl.loading.database_connection import engine
from etl.utils.logger import logger


def load_csv(file_path, table_name):

    start = time.time()

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
        chunksize=5000,
        method="multi"
    )

    end = time.time()

    logger.info(
        f"{len(df)} rows loaded into {table_name}"
    )

    logger.info(
        f"Execution Time : {round(end-start,2)} seconds"
    )