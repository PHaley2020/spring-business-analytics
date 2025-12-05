#!/usr/bin/env python3
"""
Spring Community Business Intelligence Analysis
Data Setup and Acquisition Script

This script downloads and prepares the public datasets needed for the
CompTIA Data+ portfolio project.

Usage:
    python setup_project.py
"""

import os
import zipfile
import urllib.request
import json
from pathlib import Path

# Project configuration
PROJECT_NAME = "spring-business-analytics"
HARRIS_COUNTY_FIPS = "48201"
SPRING_ZIP_CODES = ["77373", "77379", "77380", "77381", "77382", "77383", "77386", "77388", "77389"]

# Data source URLs
DATA_SOURCES = {
    "cbp_county_2022": {
        "url": "https://www2.census.gov/programs-surveys/cbp/datasets/2022/cbp22co.zip",
        "filename": "cbp22co.zip",
        "description": "Census County Business Patterns 2022 - County level"
    },
    "cbp_zipcode_2022": {
        "url": "https://www2.census.gov/programs-surveys/cbp/datasets/2022/zbp22detail.zip",
        "filename": "zbp22detail.zip",
        "description": "Census County Business Patterns 2022 - ZIP Code detail"
    },
    "cbp_us_2022": {
        "url": "https://www2.census.gov/programs-surveys/cbp/datasets/2022/cbp22us.zip",
        "filename": "cbp22us.zip",
        "description": "Census County Business Patterns 2022 - US totals"
    }
}

def create_project_structure():
    """Create the project directory structure."""
    directories = [
        f"{PROJECT_NAME}/data/raw",
        f"{PROJECT_NAME}/data/processed",
        f"{PROJECT_NAME}/data/reference",
        f"{PROJECT_NAME}/scripts",
        f"{PROJECT_NAME}/dashboards",
        f"{PROJECT_NAME}/documentation",
        f"{PROJECT_NAME}/notebooks"
    ]

    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {directory}")

    return True

def download_dataset(name, config, target_dir):
    """Download a single dataset."""
    url = config["url"]
    filename = config["filename"]
    filepath = os.path.join(target_dir, filename)

    print(f"\nDownloading {name}...")
    print(f"  URL: {url}")
    print(f"  Target: {filepath}")

    try:
        urllib.request.urlretrieve(url, filepath)
        print(f"  ✓ Downloaded successfully ({os.path.getsize(filepath) / 1024 / 1024:.1f} MB)")

        # Extract if ZIP file
        if filename.endswith('.zip'):
            extract_dir = filepath.replace('.zip', '')
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(target_dir)
            print(f"  ✓ Extracted to {target_dir}")

        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def create_readme():
    """Create the project README.md."""
    readme_content = """# Spring Community Business Intelligence Analysis

## Project Overview

A comprehensive data analytics portfolio project demonstrating mastery of all five
CompTIA Data+ (DA0-001) domains through analysis of Harris County, Texas business data.

## Curriculum Alignment

- **CompTIA Data+** (DA0-001): All 5 exam domains covered
- **LinkedIn Learning**: Data Analytics 1 Foundations (Robin Hunt)

## Data Sources

| Dataset | Source | Description |
|---------|--------|-------------|
| County Business Patterns 2022 | US Census Bureau | Establishment counts, employment, payroll by industry |
| ZIP Code Business Patterns 2022 | US Census Bureau | Business data at ZIP code level |
| NAICS Codes | US Census Bureau | Industry classification reference |

## Project Structure

```
spring-business-analytics/
├── data/
│   ├── raw/              # Original downloaded datasets
│   ├── processed/        # Cleaned and transformed data
│   └── reference/        # NAICS codes, FIPS codes, lookups
├── scripts/
│   ├── etl_pipeline.py   # Data extraction and transformation
│   ├── analysis.sql      # SQL queries for analysis
│   └── data_quality.py   # Quality validation scripts
├── notebooks/
│   └── statistical_analysis.ipynb
├── dashboards/
│   └── spring_business_dashboard.pbix
├── documentation/
│   ├── data_dictionary.md
│   ├── governance_framework.md
│   └── erd_diagram.png
└── README.md
```

## CompTIA Data+ Domain Coverage

| Domain | Weight | Project Component |
|--------|--------|-------------------|
| 1.0 Data Concepts | 15% | Schema design, data dictionary |
| 2.0 Data Mining | 25% | ETL pipeline, data cleansing |
| 3.0 Data Analysis | 23% | Statistical analysis notebook |
| 4.0 Visualization | 23% | Power BI dashboard |
| 5.0 Data Governance | 14% | Governance documentation |

## Key Analysis Questions

1. Which NAICS sectors dominate Harris County's business landscape?
2. What is the average employment per establishment by industry?
3. How does Spring's business composition compare to the county?
4. Which industries have the highest payroll-to-employment ratios?
5. What correlations exist between establishment size and annual payroll?

## Getting Started

1. Run `python setup_project.py` to download datasets
2. Execute `python scripts/etl_pipeline.py` to process data
3. Open notebooks for analysis
4. View dashboard in Power BI Desktop

## Tools Used

- **Database**: SQLite
- **Analysis**: Python (pandas, scipy), SQL
- **Visualization**: Power BI Desktop
- **Version Control**: Git/GitHub

## Author

Portfolio project for CompTIA Data+ certification preparation.

## License

Data sources are public domain (US Government).
Project code is MIT licensed.
"""

    with open(f"{PROJECT_NAME}/README.md", 'w') as f:
        f.write(readme_content)
    print(f"\n✓ Created README.md")

def create_gitignore():
    """Create .gitignore file."""
    gitignore_content = """# Data files (large)
*.zip
data/raw/*.csv
data/raw/*.txt

# Python
__pycache__/
*.py[cod]
.venv/
venv/
.env

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Jupyter
.ipynb_checkpoints/

# Power BI backups
*.pbix.bak
"""

    with open(f"{PROJECT_NAME}/.gitignore", 'w') as f:
        f.write(gitignore_content)
    print(f"✓ Created .gitignore")

def create_requirements():
    """Create requirements.txt."""
    requirements = """# Data Analytics Project Dependencies
pandas>=2.0.0
numpy>=1.24.0
scipy>=1.10.0
statsmodels>=0.14.0
matplotlib>=3.7.0
seaborn>=0.12.0
jupyter>=1.0.0
openpyxl>=3.1.0
requests>=2.28.0
"""

    with open(f"{PROJECT_NAME}/requirements.txt", 'w') as f:
        f.write(requirements)
    print(f"✓ Created requirements.txt")

def create_data_dictionary():
    """Create initial data dictionary."""
    data_dict = """# Data Dictionary

## County Business Patterns (CBP) 2022

### cbp22co.csv - County Level Data

| Field | Type | Description |
|-------|------|-------------|
| fipstate | VARCHAR(2) | FIPS State Code (48 = Texas) |
| fipscty | VARCHAR(3) | FIPS County Code (201 = Harris) |
| naics | VARCHAR(6) | NAICS Industry Code |
| emp_nf | VARCHAR(1) | Employment Noise Flag |
| emp | INTEGER | Mid-March Employment |
| qp1_nf | VARCHAR(1) | Q1 Payroll Noise Flag |
| qp1 | INTEGER | First Quarter Payroll ($1,000s) |
| ap_nf | VARCHAR(1) | Annual Payroll Noise Flag |
| ap | INTEGER | Annual Payroll ($1,000s) |
| est | INTEGER | Number of Establishments |
| n1_4 | INTEGER | Establishments with 1-4 employees |
| n5_9 | INTEGER | Establishments with 5-9 employees |
| n10_19 | INTEGER | Establishments with 10-19 employees |
| n20_49 | INTEGER | Establishments with 20-49 employees |
| n50_99 | INTEGER | Establishments with 50-99 employees |
| n100_249 | INTEGER | Establishments with 100-249 employees |
| n250_499 | INTEGER | Establishments with 250-499 employees |
| n500_999 | INTEGER | Establishments with 500-999 employees |
| n1000 | INTEGER | Establishments with 1000+ employees |
| n1000_1 | INTEGER | Establishments with 1000-1499 employees |
| n1000_2 | INTEGER | Establishments with 1500-2499 employees |
| n1000_3 | INTEGER | Establishments with 2500-4999 employees |
| n1000_4 | INTEGER | Establishments with 5000+ employees |

### Key Filter Values

- **Harris County, Texas**: fipstate = '48', fipscty = '201'
- **Spring Area ZIP Codes**: 77373, 77379, 77380, 77381, 77382, 77383, 77386, 77388, 77389

### NAICS Code Structure

| Level | Digits | Example | Description |
|-------|--------|---------|-------------|
| Sector | 2 | 44 | Retail Trade |
| Subsector | 3 | 445 | Food and Beverage Stores |
| Industry Group | 4 | 4451 | Grocery Stores |
| Industry | 5 | 44511 | Supermarkets |
| National Industry | 6 | 445110 | Supermarkets and Grocery Stores |

## Data Quality Notes

- Employment figures may be suppressed (marked with noise flags) to protect confidentiality
- Establishment size class data provides distribution when exact employment is suppressed
- NAICS "------" represents total for all industries at that geography level
"""

    with open(f"{PROJECT_NAME}/documentation/data_dictionary.md", 'w') as f:
        f.write(data_dict)
    print(f"✓ Created data_dictionary.md")

def create_etl_skeleton():
    """Create skeleton ETL pipeline script."""
    etl_script = '''#!/usr/bin/env python3
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
    print(f"\\nProfiling {name}...")
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    print(f"\\n  Missing Values:")
    print(df.isnull().sum())
    print(f"\\n  Data Types:")
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
    print("\\nTransforming data...")

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
    print(f"\\nLoading to database: {db_path}")

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

    # Find county data file
    county_file = None
    for f in os.listdir(RAW_DATA_DIR):
        if f.startswith('cbp22co') and f.endswith('.txt'):
            county_file = os.path.join(RAW_DATA_DIR, f)
            break

    if county_file is None:
        print("ERROR: County data file not found. Run setup_project.py first.")
        return

    # Execute ETL
    df_raw = extract_county_data(county_file)
    profile = profile_data(df_raw, "Harris County CBP")
    df_clean = transform_data(df_raw)

    # Save processed CSV
    processed_file = os.path.join(PROCESSED_DIR, "harris_county_cbp_2022.csv")
    df_clean.to_csv(processed_file, index=False)
    print(f"\\n✓ Saved processed data to {processed_file}")

    # Load to database
    load_to_database(df_clean, "county_business_patterns", DATABASE_PATH)

    print("\\n" + "=" * 60)
    print("ETL Pipeline Complete")
    print("=" * 60)


if __name__ == "__main__":
    run_etl_pipeline()
'''

    with open(f"{PROJECT_NAME}/scripts/etl_pipeline.py", 'w') as f:
        f.write(etl_script)
    print(f"✓ Created etl_pipeline.py")

def main():
    """Main setup routine."""
    print("=" * 60)
    print("Spring Community Business Intelligence Analysis")
    print("Project Setup Script")
    print("=" * 60)

    # Create directory structure
    print("\n1. Creating project structure...")
    create_project_structure()

    # Create project files
    print("\n2. Creating project files...")
    create_readme()
    create_gitignore()
    create_requirements()
    create_data_dictionary()
    create_etl_skeleton()

    # Download datasets
    print("\n3. Downloading datasets...")
    raw_dir = f"{PROJECT_NAME}/data/raw"

    for name, config in DATA_SOURCES.items():
        download_dataset(name, config, raw_dir)

    print("\n" + "=" * 60)
    print("Setup Complete!")
    print("=" * 60)
    print(f"\nNext steps:")
    print(f"  1. cd {PROJECT_NAME}")
    print(f"  2. pip install -r requirements.txt")
    print(f"  3. python scripts/etl_pipeline.py")
    print(f"  4. Open notebooks for analysis")


if __name__ == "__main__":
    main()
