-- ============================================================================
-- SPRING BUSINESS INTELLIGENCE - SQL QUERY LIBRARY
-- CompTIA Data+ Domain 3.4: Common data analytics tools (SQL)
-- ============================================================================

-- BASIC QUERIES
SELECT * FROM business_patterns
WHERE geography = 'Harris County' AND LENGTH(naics) = 2
ORDER BY emp DESC;

-- Total employment and establishments
SELECT
    SUM(emp) as total_employment,
    SUM(est) as total_establishments,
    ROUND(AVG(avg_emp_per_est), 2) as avg_employees_per_establishment
FROM business_patterns
WHERE geography = 'Harris County';
