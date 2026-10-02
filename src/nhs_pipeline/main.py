from .clean import load_raw_data, clean_data
from .validation import run_validations
from .database import load_csv_to_postgres
from .download import download_data
from datetime import datetime



def main():

    """ Run NHS prescription data pipeline"""

    print("Starting pipeline")

    #Extract data and store as RAW JSON
    download_data()


    print("Loading raw data")
    df = load_raw_data()

    #Transform Raw Data before analysis
    print("Cleaning data")
    clean_df = clean_data(df)


    # Run validation
    print("Running validations")
    errors = run_validations(
        clean_df,
        datetime.today()
    )


    if errors:
        print("Validation failed:")
        print(errors)
        return


    print("Saving cleaned CSV")
    clean_df.to_csv(
        "data/processed/epd_clean.csv",
        index=False
    )


    print("Loading into PostgreSQL")
    load_csv_to_postgres(
        "data/processed/epd_clean.csv"
    )


    print("Pipeline completed successfully")


if __name__ == "__main__":
    main()