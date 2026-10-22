# Customer Data Cleaning Tool

A beginner-friendly data cleaning project built with Python and Pandas.

## Project Overview

This project cleans a sample customer dataset stored in CSV format.
It standardizes text values, identifies duplicate customer records,
checks email formats, preserves missing values for review, and creates
a summary report.

## Features

- Loads customer data from a CSV file.
- Removes leading and trailing whitespace.
- Standardizes customer names and city names.
- Converts email addresses to lowercase.
- Identifies and removes duplicate customer records using name, email,
  and city, excluding customer_id from the comparison.
- Detects missing values.
- Checks email address formats.
- Exports cleaned data and a summary report.

## Technologies

- Python
- Pandas
- Regular expressions
- Google Colab

## Project Structure

```text
customer-data-cleaning-tool/
├── data/
│   ├── original_data.csv
│   └── cleaned_data.csv
├── src/
│   └── clean_data.py
├── reports/
│   └── summary_report.txt
└── README.md
```

## How to Run

1. Open the notebook in Google Colab.
2. Mount Google Drive.
3. Ensure the original CSV is saved in the data folder.
4. Run the cleaning program:

   `%run /content/my_drive/MyDrive/customer-data-cleaning-tool/src/clean_data.py`

5. Review cleaned_data.csv and summary_report.txt.

## Sample Results

- Original records: 20
- Cleaned records: 18
- Duplicate customer records removed: 2
- Invalid non-empty email formats detected: 2

These results refer to the sample dataset included with this project.

## Data Quality Notes

Missing names, emails, and cities are preserved for review.
Invalid email formats are flagged rather than silently deleted.
Email validation checks format only; it does not confirm that an
email address exists.

## Future Improvements

- Add automated unit tests.
- Add configurable duplicate matching rules.
- Export a separate file containing invalid email records.
- Add data quality charts and a more detailed report.

## Author

Add your name and portfolio links here.
