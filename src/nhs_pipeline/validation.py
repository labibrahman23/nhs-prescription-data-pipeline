import pandas as pd



def number_validation(df):

    """ Check numeric values in data set are not negative """


    #Collect numeric columns into a list 
    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    errors=[]

    #Check each column for negative values and append error to list 
    for column in numeric_columns:
        
        negative_values = df[column] <0
        if negative_values.any():
            errors.append(f"There are negative values in, {column}")

    
    
    return errors



def date_validation(df, current_date):

    """ Check all dates are within correct range """

    # This start data is when NHS prescription data began releasing 
    start_date= pd.to_datetime("2011-12-31")
    end_date = pd.to_datetime(current_date)

    errors = []


    # check values are before minimum date, append error data
    invalid_dates = df["year_month"] < start_date
    if invalid_dates.any():
        errors.append(f"{invalid_dates.sum()} are invalid, they are before start data of: {start_date}")


    # check no dates are in the future 
    future_dates = df["year_month"] > end_date
    if future_dates.any():
        errors.append(f"{future_dates.sum()} are invalid, they are after the data limit of : {current_date}")

    return errors


def schema_validation(df):

    """Ensure required columns are present and of correct data type """

    schema_errors = []

    #Create required columns list and match against dataset columns, appending any missing
    required_columns=['year_month','regional_office_name','items','quantity','total_quantity','actual_cost','snomed_code']
    columns =df.columns.tolist()

    for item in required_columns:
        if item not in columns:

            schema_errors.append(f"Missing Required column : {item}")



    #check data is correct data type, mapping data to its data type

    key_to_data_type= {

        'year_month' : 'datetime64[us]',
        'regional_office_name': 'str',
        'items': 'Int64',
        'quantity': 'Int64',
        'total_quantity': 'Int64',
        'actual_cost': 'float64',
        'snomed_code' : 'str'

    }

    for key, data_type in key_to_data_type.items():

        if key in df.columns and df[key].dtype != data_type:
            schema_errors.append(f"{key} is saved incorrectly as {df[key].dtype}, it should be {data_type} \n")
            

    
    return schema_errors





def run_validations(df, current_date):

    """ Run all validations, before loading Data to PostGreSQL"""

    errors_list = []


    schema_errors = schema_validation(df)
    errors_list.extend(schema_errors)


    invalid_dates = date_validation(df, current_date)
    errors_list.extend(invalid_dates)


    invalid_numbers = number_validation(df)
    errors_list.extend(invalid_numbers)


    return errors_list


