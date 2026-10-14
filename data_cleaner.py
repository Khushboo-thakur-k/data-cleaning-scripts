import pandas as pd
import os

def clean_dataset(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} was not found.")
        return None

    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path)
    else:
        print("Unsupported file format!")
        return None

    print(f"Original rows: {len(df)}")

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna('N/A')

    # Clean text columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    print(f"Cleaned rows: {len(df)}")
    
    output_file = "cleaned_output.csv"
    df.to_csv(output_file, index=False)
    print(f"Cleaned file successfully saved as: {output_file}")
    return df
