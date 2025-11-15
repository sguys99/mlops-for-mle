# data_generator.py
import time
from argparse import ArgumentParser
from datetime import datetime

import pandas as pd
from sklearn.datasets import load_iris
from sqlalchemy import create_engine, text


def get_data():
    X, y = load_iris(return_X_y=True, as_frame=True)
    df = pd.concat([X, y], axis="columns")
    rename_rule = {
        "sepal length (cm)": "sepal_length",
        "sepal width (cm)": "sepal_width",
        "petal length (cm)": "petal_length",
        "petal width (cm)": "petal_width",
    }
    df = df.rename(columns=rename_rule)
    return df


def create_table(engine):
    """Create iris_data table using raw SQL query."""
    create_table_query = """
        CREATE TABLE IF NOT EXISTS iris_data (
        id SERIAL PRIMARY KEY,
        timestamp timestamp,
        sepal_length float8,
        sepal_width float8,
        petal_length float8,
        petal_width float8,
        target int
    );
    """
    print(create_table_query)
    with engine.connect() as conn:
        conn.execute(create_table_query)
        conn.commit()


def insert_data(engine, data):
    """Insert a single row of data using SQL query."""
    insert_query = f"""
    INSERT INTO iris_data
        (timestamp, sepal_length, sepal_width, petal_length, petal_width, target)
        VALUES (
            NOW(),
            {data.sepal_length},
            {data.sepal_width},
            {data.petal_length},
            {data.petal_width},
            {data.target}
        );
    """
    print(insert_query)
    with engine.connect() as conn:
        conn.execute(insert_query)
        conn.commit()


def generate_data(engine, df):
    """Continuously generate and insert random iris data samples."""
    while True:
        insert_data(engine, df.sample(1).squeeze())
        time.sleep(1)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--db-host", dest="db_host", type=str, default="localhost")
    args = parser.parse_args()

    # Format: postgresql://user:password@host:port/database
    db_url = (
        f"postgresql://myuser:mypassword@{args.db_host}:5432/mydatabase"
    )
    engine = create_engine(db_url, echo=False)

    # Create table
    create_table(engine)

    # # Load iris dataset
    # df = get_data()

    # # Start continuous data generation
    # print("Starting data generation... (Press Ctrl+C to stop)")
    # try:
    #     generate_data(engine, df)
    # except KeyboardInterrupt:
    #     print("\nData generation stopped.")
    # finally:
    #     engine.dispose()
