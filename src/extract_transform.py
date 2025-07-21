import pandas as pd

def extract_and_transform(csv_path='data/raw-data.csv'):
    # Extract
    sales_data = pd.read_csv(csv_path)

    # Remove PII
    pii_fields = ['Customer Name', 'Card Number']
    sales_data = sales_data.drop(columns=[col for col in pii_fields if col in sales_data.columns])

    # Definefields
    required_fields = ['Drink', 'Qty', 'Price', 'Branch', 'Payment Type', 'Date/Time']

    # Define incomplete rows
    def is_incomplete(row):
        return not all(pd.notna(row.get(field)) and str(row.get(field)).strip() != '' for field in required_fields)

    # 5. Filter complete rows
    incomplete_rows = sales_data[sales_data.apply(is_incomplete, axis=1)]
    clean_sales = sales_data[~sales_data.index.isin(incomplete_rows.index)]

    return clean_sales