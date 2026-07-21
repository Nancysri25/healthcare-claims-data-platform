from sqlalchemy import inspect, text

from etl.loading.database_connection import engine
from etl.utils.logger import logger


def postgres_upsert(table_name, primary_key):

    inspector = inspect(engine)

    columns = [
        col["name"]
        for col in inspector.get_columns(table_name)
        if col["name"] != "created_at"
    ]

    staging_table = f"{table_name}_staging"

    insert_columns = ", ".join(columns)

    select_columns = ", ".join(columns)

    update_columns = ", ".join(
        [
            f"{col}=EXCLUDED.{col}"
            for col in columns
            if col != primary_key
        ]
    )

    sql = f"""
    INSERT INTO {table_name} ({insert_columns})
    SELECT {select_columns}
    FROM {staging_table}

    ON CONFLICT ({primary_key})
    DO UPDATE
    SET {update_columns};
    """

    with engine.begin() as conn:

        updated = conn.execute(
            text(f"""
                SELECT COUNT(*)
                FROM {staging_table} s
                JOIN {table_name} t
                  ON s.{primary_key} = t.{primary_key}
            """)
        ).scalar()

        inserted = conn.execute(
            text(f"""
                SELECT COUNT(*)
                FROM {staging_table} s
                LEFT JOIN {table_name} t
                  ON s.{primary_key} = t.{primary_key}
                WHERE t.{primary_key} IS NULL
            """)
        ).scalar()

        conn.execute(text(sql))

        conn.execute(
            text(f"DROP TABLE IF EXISTS {staging_table}")
        )

        logger.info(f"Inserted : {inserted}")
        logger.info(f"Updated  : {updated}")