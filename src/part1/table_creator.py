# table_creator.py
from sqlalchemy import create_engine, text


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
        conn.execute(text(create_table_query))
        conn.commit()



if __name__ == "__main__":

    # Format: postgresql://user:password@host:port/database
    db_url = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
    
    engine = create_engine(db_url, echo=False)

    create_table(engine)

