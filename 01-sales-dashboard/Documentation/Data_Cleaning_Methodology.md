# Data Cleaning Methodology — Small Business Sales Dashboard

## 1. Purpose

This document describes the data review and validation steps performed for the Small Business Sales Dashboard project using Microsoft Excel.

The dataset contains 100 fictional sales records prepared for learning and portfolio purposes.

## 2. Source Data

The original sales records were stored in the `Raw_Data` worksheet of the Excel workbook.

The data includes Order ID, Order Date, Product, Category, Quantity, Unit Price, Sales, and Region.

## 3. Preparation of Clean_Data

A separate worksheet named `Clean_Data` was created by copying the records from `Raw_Data`.

This worksheet was used to review the data and perform validation checks.

## 4. Data Quality Checks

### 4.1 Missing Values

The dataset was checked for blank cells.

This check was performed to identify potentially incomplete records.

### 4.2 Duplicate Records

The dataset was checked for duplicate records.

Duplicate records were not removed as part of the documented process.

### 4.3 Sales Calculation Validation

A `Sales_Check` column was added to compare the expected sales calculation with the recorded sales value.

The formula used was:

`=E2*F2`

This calculates Quantity multiplied by Unit Price.

The formula was filled down for the available records.

### 4.4 Summary Metrics

The Excel summary formulas were used to calculate:

- Total Sales
- Total Orders
- Total Quantity
- Average Order Value

## 5. Tools Used

- Microsoft Excel
- Excel worksheets
- Excel formulas
- PivotTables

## 6. Limitations

- The dataset contains fictional records and does not represent verified real-world business transactions.
- Checking for missing values and duplicates does not, by itself, prove that every record is accurate.
- Duplicate records were checked but not removed.
- The currency unit and exact dataset date range have not been confirmed in this document.
- The `Sales_Check` formula provides a calculated value; any differences between this value and recorded Sales should be reviewed before drawing conclusions.

## 7. Conclusion

The data preparation process created a separate worksheet for review, checked for missing and duplicate values, and added a calculation column to support sales validation.

These steps provide a documented basis for the Excel sales analysis and dashboard.