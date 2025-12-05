# Data Dictionary

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
