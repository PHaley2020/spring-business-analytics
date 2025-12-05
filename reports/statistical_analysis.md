# Statistical Analysis Report

**Project:** Spring Community Business Intelligence Analysis
**Date:** 2025-12-05
**Analyst:** Data+ Portfolio Project

---
## 1. Descriptive Statistics

*CompTIA Data+ Domain 3.1: Measures of central tendency and dispersion*

### 1.1 Employment by Sector

| Measure | Value |
|---------|-------|
| Count (n) | 24 |
| Mean | 18,359 |
| Median | 15,662 |
| Std Deviation | 13,877 |
| Min | 2,509 |
| Max | 52,353 |
| Range | 49,844 |

### 1.2 Establishments by Sector

| Measure | Value |
|---------|-------|
| Mean | 1,059 |
| Median | 1,090 |
| Std Deviation | 572 |

### 1.3 Annual Payroll by Sector ($1,000s)

| Measure | Value |
|---------|-------|
| Mean | $850,596 |
| Median | $872,216 |
| Std Deviation | $556,434 |

---
## 2. Frequency Analysis

### 2.1 Top 10 Sectors by Employment

| Rank | Sector | Employment | % of Total |
|------|--------|------------|------------|
| 1 | Accommodation and Food Services | 52,353 | 11.9% |
| 2 | Retail Trade - Electronics/Food | 49,696 | 11.3% |
| 3 | Arts and Entertainment | 38,262 | 8.7% |
| 4 | Transportation - Postal/Warehouse | 32,580 | 7.4% |
| 5 | Retail Trade - Motor/Furniture | 30,375 | 6.9% |
| 6 | Construction | 28,752 | 6.5% |
| 7 | Manufacturing - Metal/Electronics | 22,000 | 5.0% |
| 8 | Transportation - Air/Rail/Water | 21,846 | 5.0% |
| 9 | Manufacturing - Wood/Chemical | 20,655 | 4.7% |
| 10 | Public Administration | 19,459 | 4.4% |

### 2.2 Top 10 Sectors by Establishment Count

| Rank | Sector | Establishments | % of Total |
|------|--------|----------------|------------|
| 1 | Accommodation and Food Services | 1,939 | 7.6% |
| 2 | Arts and Entertainment | 1,822 | 7.2% |
| 3 | Construction | 1,797 | 7.1% |
| 4 | Public Administration | 1,769 | 7.0% |
| 5 | Transportation - Postal/Warehouse | 1,629 | 6.4% |
| 6 | Information | 1,555 | 6.1% |
| 7 | Retail Trade - Electronics/Food | 1,553 | 6.1% |
| 8 | Finance and Insurance | 1,507 | 5.9% |
| 9 | Wholesale Trade | 1,441 | 5.7% |
| 10 | Manufacturing - Wood/Chemical | 1,377 | 5.4% |

---
## 3. Correlation Analysis

*CompTIA Data+ Domain 3.2: Inferential statistical methods*

### 3.1 Correlation Matrix

| Variable 1 | Variable 2 | Correlation | Interpretation |
|------------|------------|-------------|----------------|
| Employment | Establishments | 0.731 | Strong positive |
| Employment | Annual Payroll | 0.896 | Strong positive |
| Establishments | Annual Payroll | 0.805 | Strong positive |

**Key Finding:** Strong positive correlations between all three variables 
indicate that sectors with more establishments tend to have proportionally 
higher employment and payroll, suggesting consistent business scaling patterns.

---
## 4. Comparative Analysis: Spring vs Harris County

*CompTIA Data+ Domain 3.3: Trend and performance analysis*

### 4.1 Employment Distribution Comparison

| Sector | Harris County | Spring Area | Spring % of County |
|--------|---------------|-------------|-------------------|
| Accommodation and Food Service | 52,353 | 10,917 | 20.9% |
| Retail Trade - Electronics/Foo | 49,696 | 7,379 | 14.8% |
| Retail Trade - Motor/Furniture | 30,375 | 7,817 | 25.7% |

---
## 5. Hypothesis Testing Framework

*CompTIA Data+ Domain 3.2: Hypothesis testing, Type I/II errors*

### 5.1 Test: Small Business Dominance

- **H₀ (Null):** Small businesses (1-19 employees) do not dominate Harris County

- **H₁ (Alternative):** Small businesses represent >70% of establishments


**Result:** Average small business percentage = 79.2%

**Conclusion:** Reject H₀. Small businesses significantly dominate the market.

### 5.2 Potential Type I and Type II Errors

| Error Type | Description | Business Impact |
|------------|-------------|-----------------|
| Type I (α) | Concluding small biz dominance when false | Over-investment in small biz programs |
| Type II (β) | Missing true small biz dominance | Under-serving key market segment |

---
## 6. Key Insights Summary

### Business Landscape Findings

1. **Largest Employment Sector:** Accommodation and Food Services with 52,353 employees
2. **Highest Paying Sector:** Finance and Insurance at $91,773 average per employee
3. **Small Business Rate:** 79.2% of establishments have <20 employees
4. **Total County Employment:** 440,606 across 24 sectors
5. **Strong Correlation:** Employment and payroll highly correlated (r=0.90)