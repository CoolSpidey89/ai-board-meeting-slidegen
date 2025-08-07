import pandas as pd
import pdfplumber

def parse_file(file):
    filename = file.name.lower()

    if filename.endswith(".csv"):
        df = pd.read_csv(file)
        return parse_financial_df(df), df

    elif filename.endswith((".xlsx", ".xls")):
        df = pd.read_excel(file)
        return parse_financial_df(df), df

    elif filename.endswith(".pdf"):
        return parse_pdf_reviews(file), None

    else:
        raise ValueError("Unsupported file format.")

def parse_financial_df(df):
    required_cols = ['Revenue', 'Cost', 'Churn', 'Region', 'Month']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"Missing required columns. Found: {df.columns.tolist()}")

    df = df.dropna(subset=required_cols)

    metrics = {
        'total_revenue': df['Revenue'].sum(),
        'total_cost': df['Cost'].sum(),
        'avg_churn': round(df['Churn'].mean(), 2),
        'regions': df['Region'].unique().tolist(),
        'monthly_data': df.groupby('Month').agg({
            'Revenue': 'sum',
            'Cost': 'sum',
            'Churn': 'mean'
        }).reset_index()
    }

    return metrics

def parse_pdf_reviews(file):
    with pdfplumber.open(file) as pdf:
        all_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text += text + "\n"

    cleaned_text = all_text.strip()
    if not cleaned_text:
        raise ValueError("No text could be extracted from the PDF.")

    return {
        'user_reviews': cleaned_text
    }
