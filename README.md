# Spring Community Business Intelligence Analysis

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
