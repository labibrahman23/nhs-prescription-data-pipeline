import psycopg2

def create_connection():


    """Create and return a connection to the PostgreSQL database.
    Database credentials are loaded from environment variables
    stored in a .env file.
    """

    connection = psycopg2.connect(
    host=("localhost"),
    port=("5432"),
    database=("uk_job_market_data"),
    user=("postgres"),
    password=("LabibDataProjects")
    )

    

    return connection


def load_csv_to_postgres(csv_path):

    
    """Load cleaned CSV data into PostgreSQL using COPY."""


    

    connection = create_connection()

    with connection.cursor() as cursor:

        with open("sql/load_data.sql", "r") as sql_file:
            query = sql_file.read()

        with open(csv_path, "r") as file:
            cursor.copy_expert(query,file)

    connection.commit()

    connection.close()

    

    
