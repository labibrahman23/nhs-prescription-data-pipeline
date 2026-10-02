def dataset_information(df):


    """ Explore raw data set, finding data types, shapes and possible errors """

    
    print("\n  Data set information: ")
    df.info()

    print("\n  Data set rows and columns: ")
    print(df.shape)

    print("\n  Number of null values: ")
    print(df.isnull().sum())

    
    print("\n  Number of duplicate values ")
    print(df.duplicated().sum())


    print("\n  Column names ")
    print(df.columns.tolist())
    
    print("\n  Data types:")
    print(df.dtypes)