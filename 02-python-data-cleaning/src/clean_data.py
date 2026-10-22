
from pathlib import Path
from datetime import datetime
import re
import pandas as pd

# Project folders
PROJECT_PATH = Path(
    "/content/my_drive/MyDrive/customer-data-cleaning-tool"
)
DATA_PATH = PROJECT_PATH / "data"
REPORT_PATH = PROJECT_PATH / "reports"

INPUT_FILE = DATA_PATH / "original_data.csv"
OUTPUT_FILE = DATA_PATH / "cleaned_data.csv"
SUMMARY_FILE = REPORT_PATH / "summary_report.txt"


def is_valid_email(email):
    """Check an email using a simple validation rule."""
    if not email:
        return False

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(pattern, email) is not None


def clean_text(value):
    """Remove unnecessary spaces and convert blank text to missing."""
    if pd.isna(value):
        return pd.NA

    value = str(value).strip()

    if value == "":
        return pd.NA

    return value


def clean_customers():
    """Load, inspect, clean and report customer data."""

    if not INPUT_FILE.exists():
        print("ERROR: Original CSV file was not found.")
        print("Expected location:", INPUT_FILE)
        print("Please check the project folder and try again.")
        return

    DATA_PATH.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.mkdir(parents=True, exist_ok=True)

    # Load original CSV
    df = pd.read_csv(INPUT_FILE, dtype=str, keep_default_na=False)

    original_rows = len(df)
    original_columns = list(df.columns)

    print("CUSTOMER DATA CLEANING TOOL")
    print("=" * 35)
    print("Original records:", original_rows)
    print("Columns:", original_columns)

    # Convert whitespace-only cells to missing values
    for column in df.columns:
        df[column] = df[column].map(clean_text)

    # Count missing values before cleaning
    missing_before = {}
    for column in df.columns:
        count = int(df[column].isna().sum())
        if count > 0:
            missing_before[column] = count

    # Identify and remove exact duplicate records
    # Standardize text before checking duplicate customer records.
    if "name" in df.columns:
        df["name"] = df["name"].map(
            lambda value: value.title() if pd.notna(value) else pd.NA
        )

    if "city" in df.columns:
        df["city"] = df["city"].map(
            lambda value: value.title() if pd.notna(value) else pd.NA
        )

    if "email" in df.columns:
        df["email"] = df["email"].map(
            lambda value: value.strip().lower() if pd.notna(value) else pd.NA
        )

    # Compare customer details, excluding customer_id.
    duplicate_columns = [
        column for column in ["name", "email", "city"]
        if column in df.columns
    ]

    duplicate_count = int(
        df.duplicated(subset=duplicate_columns).sum()
    )

    df = df.drop_duplicates(
        subset=duplicate_columns,
        keep="first"
    ).copy()

    # Standardize names: trim spaces and use title case
    if "name" in df.columns:
        df["name"] = df["name"].map(
            lambda value: value.title() if pd.notna(value) else pd.NA
        )

    # Standardize city names
    if "city" in df.columns:
        df["city"] = df["city"].map(
            lambda value: value.title() if pd.notna(value) else pd.NA
        )

    # Normalize email spaces and case, without inventing missing emails
    if "email" in df.columns:
        df["email"] = df["email"].map(
            lambda value: value.strip().lower()
            if pd.notna(value) else pd.NA
        )

    # Find invalid and missing email values
    invalid_email_mask = pd.Series(False, index=df.index)
    missing_email_count = 0

    if "email" in df.columns:
        missing_email_count = int(df["email"].isna().sum())

        invalid_email_mask = df["email"].map(
            lambda value: not is_valid_email(value)
            if pd.notna(value) else False
        )

    invalid_email_count = int(invalid_email_mask.sum())
    invalid_email_records = df.loc[invalid_email_mask].copy()

    # Preserve all non-duplicate records, including missing/invalid values.
    # No customer rows are deleted because of missing or invalid fields.
    cleaned_rows = len(df)

    # Save cleaned CSV. Empty fields represent missing values.
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    # Build a human-readable summary report
    report_lines = [
        "CUSTOMER DATA CLEANING TOOL - SUMMARY REPORT",
        "=" * 48,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"Original record count: {original_rows}",
        f"Duplicate customer records removed: {duplicate_count}",
        f"Cleaned record count: {cleaned_rows}",
        f"Records removed in total: {original_rows - cleaned_rows}",
        "",
        "Missing values before cleaning:",
    ]

    if missing_before:
        for column, count in missing_before.items():
            report_lines.append(f"- {column}: {count}")
    else:
        report_lines.append("- No missing values found")

    report_lines.extend([
        "",
        f"Missing email values after cleaning: {missing_email_count}",
        f"Invalid non-empty email count: {invalid_email_count}",
        "",
        "Invalid non-empty email values:",
    ])

    if invalid_email_count > 0:
        for value in invalid_email_records["email"].tolist():
            report_lines.append(f"- {value}")
    else:
        report_lines.append("- None")

    report_lines.extend([
        "",
        "ACTIONS PERFORMED",
        "- Loaded the original CSV file.",
        "- Detected blank and whitespace-only values.",
        "- Identified and removed duplicate customer records using name, email, and city.",
        "- Trimmed unnecessary spaces from text fields.",
        "- Standardized non-missing names and city names to title case.",
        "- Converted email addresses to lowercase and trimmed spaces.",
        "- Validated non-empty email addresses using a simple rule.",
        "- Preserved missing values; did not invent customer information.",
        "- Preserved rows with missing or invalid values for review.",
        "- Saved the cleaned CSV and this summary report.",
        "",
        "LIMITATIONS",
        "- Email validation is a basic format check, not proof that an address exists.",
        "- Duplicate detection compares name, email, and city; customer_id is excluded.",
        "- Similar customer records are not automatically merged.",
    ])

    SUMMARY_FILE.write_text(
        "\n".join(report_lines) + "\n",
        encoding="utf-8"
    )

    # Show results
    print("\nCleaning completed!")
    print("Duplicate customer records removed:", duplicate_count)
    print("Missing values before cleaning:", missing_before)
    print("Invalid non-empty emails:", invalid_email_count)
    print("Cleaned records:", cleaned_rows)
    print("\nCleaned CSV:", OUTPUT_FILE)
    print("Summary report:", SUMMARY_FILE)


if __name__ == "__main__":
    clean_customers()

    
