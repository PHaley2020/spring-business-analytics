#!/usr/bin/env python3
"""
ETL Pipeline for Spring Business Intelligence Project
CompTIA Data+ Domain 2.0: Data Mining

This script extracts, transforms, and loads Census Bureau
County Business Patterns data into SQLite for analysis.
"""

import pandas as pd
import sqlite3
import os
from pathlib import Path

# Configuration
RAW_DATA_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
DATABASE_PATH = "data/spring_business.db"

# Harris County, Texas FIPS codes
FIPS_STATE = "48"
FIPS_COUNTY = "201"

# Spring area ZIP codes
SPRING_ZIPS = ["77373", "77379", "77380", "77381", "77382", "77383", "77386", "77388", "77389"]


def extract_county_data(filepath):
    """
    Extract and filter CBP county data for Harris County.

    CompTIA Data+ Alignment:
    - 2.1: Data acquisition concepts
    - 2.2: Data profiling
    """
    print(f"Extracting data from {filepath}...")

    # Read CSV
    df = pd.read_csv(filepath, dtype=str)

    # Filter for Harris County, Texas
    df_harris = df[(df['fipstate'] == FIPS_STATE) & (df['fipscty'] == FIPS_COUNTY)].copy()

    print(f"  Total records: {len(df)}")
    print(f"  Harris County records: {len(df_harris)}")

    return df_harris


def profile_data(df, name="dataset"):
    """
    Generate data profiling report.

    CompTIA Data+ Alignment:
    - 2.2: Cleansing and profiling datasets
    """
    print(f"\nProfiling {name}...")
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    print(f"\n  Missing Values:")
    print(df.isnull().sum())
    print(f"\n  Data Types:")
    print(df.dtypes)

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict()
    }


def transform_data(df):
    """
    Clean and transform data for analysis.

    CompTIA Data+ Alignment:
    - 2.3: Data manipulation techniques
    - 2.4: Query optimization concepts
    """
    print("\nTransforming data...")

    # Convert numeric columns
    numeric_cols = ['emp', 'qp1', 'ap', 'est', 'n1_4', 'n5_9', 'n10_19',
                   'n20_49', 'n50_99', 'n100_249', 'n250_499', 'n500_999', 'n1000']

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Handle missing values
    df['emp'] = df['emp'].fillna(0)
    df['est'] = df['est'].fillna(0)

    # Create derived variables
    df['avg_emp_per_est'] = df.apply(
        lambda x: x['emp'] / x['est'] if x['est'] > 0 else 0, axis=1
    )

    df['avg_annual_payroll_per_emp'] = df.apply(
        lambda x: (x['ap'] * 1000) / x['emp'] if x['emp'] > 0 else 0, axis=1
    )

    # Extract NAICS sector (first 2 digits)
    df['naics_sector'] = df['naics'].str[:2]

    print(f"  Derived variables created")
    print(f"  Final shape: {df.shape}")

    return df


def load_to_database(df, table_name, db_path):
    """
    Load transformed data into SQLite database.

    CompTIA Data+ Alignment:
    - 2.1: ETL/ELT processes
    """
    print(f"\nLoading to database: {db_path}")

    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Verify load
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"  Loaded {count} records to {table_name}")

    conn.close()
    return count


def run_etl_pipeline():
    """Execute the full ETL pipeline."""
    print("=" * 60)
    print("Spring Business Intelligence - ETL Pipeline")
    print("=" * 60)

    # Ensure directories exist
    Path(PROCESSED_DIR).mkdir(parents=True, exist_ok=True)

    # Find county data file (support both .txt and .csv extensions)
    county_file = None
    for f in os.listdir(RAW_DATA_DIR):
        if f.startswith('cbp22co') and (f.endswith('.txt') or f.endswith('.csv')):
            county_file = os.path.join(RAW_DATA_DIR, f)
            break

    if county_file is None:
        print("ERROR: County data file not found.")
        print(f"Looking for files starting with 'cbp22co' in {RAW_DATA_DIR}/")
        print("Run setup_project.py first or place the CBP county file in data/raw/")
        return

    # Execute ETL
    df_raw = extract_county_data(county_file)
    profile = profile_data(df_raw, "Harris County CBP")
    df_clean = transform_data(df_raw)

    # Save processed CSV
    processed_file = os.path.join(PROCESSED_DIR, "harris_county_cbp_2022.csv")
    df_clean.to_csv(processed_file, index=False)
    print(f"\n✓ Saved processed data to {processed_file}")

    # Load to database
    load_to_database(df_clean, "county_business_patterns", DATABASE_PATH)

    print("\n" + "=" * 60)
    print("ETL Pipeline Complete")
    print("=" * 60)


if __name__ == "__main__":
    run_etl_pipeline()
