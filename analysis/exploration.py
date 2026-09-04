import pandas as pd
from nhs_pipeline.database import create_connection


def get_column_names(connection):
    """ Return column names from cleaned prescription data  """


    query = """
    SELECT column_name
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE table_name = 'prescriptions';
    """

    return pd.read_sql(query,connection)



def get_number_of_rows(connection):

    """ Return the number of rows in the cleaned NHS Prescription data set"""
    query = """
    SELECT COUNT (*)
    FROM prescriptions;
    """

    result = pd.read_sql(query,connection)

    return result.iloc[0,0]


def get_data_types(connection):
    """ Get the data types for each column from prescription data """

    query = """
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE table_name = 'prescriptions';
    """

    return pd.read_sql(query,connection)

    


def get_sample_data(connection):

    """ Get 10 records as sample data """

    query = """
    SELECT *
    FROM prescriptions
    LIMIT 10;
    """

    return pd.read_sql(query,connection)

def main():

    """ Explore cleaned dataset from PostgreSQL """

    
    connection = create_connection()

    #column names
    print("\n Column names: \n  ")
    print(get_column_names(connection))


    #number of rows 
    print("\n Number of rows : \n  ")
    print(get_number_of_rows(connection))


     #Data types 
    print("\n Data Types : \n  ")
    print(get_data_types(connection))
    
    
    #sample data
    print("\n Sample data: \n  ")
    print(get_sample_data(connection))


    connection.close()


if __name__ == "__main__":
    main()
