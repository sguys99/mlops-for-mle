# data_insertion.py

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
        conn.execute(text(insert_query))
        conn.commit()


if __name__ == "__main__":

    # Format: postgresql://user:password@host:port/database
    db_url = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
    
    engine = create_engine(db_url, echo=False)

    df = get_data()
    insert_data(engine, df.sample(1).squeeze())