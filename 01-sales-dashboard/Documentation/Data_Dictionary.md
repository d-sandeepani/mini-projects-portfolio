# Data Dictionary — Small Business Sales Dashboard

## 1. Project Information

- **Project Name:** Small Business Sales Dashboard
- **Business:** NovaTech Electronics (fictional)
- **Tool:** Microsoft Excel
- **Dataset Size:** 100 sales records
- **Purpose:** To describe the fields used in the sales dataset.

## 2. Dataset Fields

| Column | Field Name | Description | Data Type |
|---|---|---|---|
| A | Order ID | Identifier assigned to a sales order record. | Text |
| B | Order Date | Date associated with the sales record. | Date |
| C | Product | Name of the product sold. | Text |
| D | Category | Product category recorded in the dataset. | Text |
| E | Quantity | Number of units recorded for the sale. | Whole number |
| F | Unit Price | Price recorded for one unit of the product. | Number |
| G | Sales | Sales value recorded for the order. | Number |
| H | Region | Region associated with the sales record. | Text |

## 3. Sales Calculation

The expected sales calculation is:

Sales = Quantity × Unit Price

In Excel, the calculation can be written as:

`=E2*F2`

This formula assumes that Quantity is in column E and Unit Price is in column F.

## 4. Additional Validation Field

| Field Name | Description |
|---|---|
| Sales_Check | A calculated value used to compare Quantity × Unit Price with the recorded Sales value. |

The Sales_Check field was added during the project validation process.

## 5. Notes and Limitations

- The dataset contains fictional records prepared for learning and portfolio purposes.
- The currency unit has not been specified in this document.
- The exact date range should be confirmed from the workbook before being documented.
- Field descriptions explain the dataset structure and do not represent verified real-world business information.