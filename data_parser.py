import pandas as pd

def parse_excel(file):
    df = pd.read_excel(file)

    required_cols = ['Revenue', 'Cost', 'Churn', 'Region', 'Month']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"Missing required columns. Found: {df.columns.tolist()}")

    # Drop rows with missing important data
    df = df.dropna(subset=required_cols)

    metrics = {}
    metrics['total_revenue'] = df['Revenue'].sum()
    metrics['total_cost'] = df['Cost'].sum()
    metrics['avg_churn'] = round(df['Churn'].mean(), 2)
    metrics['regions'] = df['Region'].unique().tolist()

    metrics['monthly_data'] = df.groupby('Month').agg({
        'Revenue': 'sum',
        'Cost': 'sum',
        'Churn': 'mean'
    }).reset_index()

    return metrics, df

