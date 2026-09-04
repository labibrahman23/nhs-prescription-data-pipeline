import json
import pandas as pd


def load_raw_data():

    """ Load the raw NHS prescription data into pandas DataFrame """

    with open("data/raw/epd1.json", "r") as file:
        data = json.load(file)
    
    # Create a dataframe from records ( the target data )
    records = data["result"]["records"]
    df = pd.DataFrame(records)
    return df



def clean_data(df):
    """ Clean and transform NHS prescription Data  """



    # Changing column names to lower case for consistent access
    df.columns = df.columns.str.lower()
    
    
    #cleaning change date to correct data type
    df["year_month"] = pd.to_datetime(df["year_month"])
    
    
    #filling missing 'snomed' values with a placeholder
    df["snomed_code"] = df["snomed_code"].fillna("Unknown")




    # Convert integer columns to numerical values ( Int64 )

    integer_columns = [
        "quantity",
        "items",
        "total_quantity",
        ]

    for column in integer_columns:
        df[column] = pd.to_numeric(
        df[column],
        errors="coerce").round().astype("Int64")
        
    # Convert decimal columns to numeric values 
    decimal_columns = [
        "adq_usage",
        "nic",
        "actual_cost"
        ]

    for column in decimal_columns:
        df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
        )

    
    # Dropping unnecessary address columns  
    df = df.drop(columns=[
        "address_1",
        "address_2",
        "address_3",
        "address_4"
        ]
        )
    
    # Map the Unidentified column to boolean values 
    df["unidentified"] = df["unidentified"].map({
    "Y": True,
    "N": False
    
    })
    
    return df
