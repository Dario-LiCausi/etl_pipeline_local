from extract_transform import extract_and_transform
from load import load_to_mysql
import pandas as pd

def main():
    pd.set_option('display.max_rows', None)

    # File path
    file_path = "data/raw-data.csv"
    print(f"Using default CSV path: {file_path}")

    # Extract and transform
    clean_sales = extract_and_transform(file_path)
    print("\nCleaned sales data:\n")
    print(clean_sales)

    # Load to db
    choice = input("\nDo you want to load this data into MySQL? (y/n): ").lower().strip()
    if choice == 'y':
        load_to_mysql(clean_sales)
        print("✅ Data successfully loaded into MySQL.")
    else:
        print("❌ Data not loaded.")

if __name__ == '__main__':
    main()