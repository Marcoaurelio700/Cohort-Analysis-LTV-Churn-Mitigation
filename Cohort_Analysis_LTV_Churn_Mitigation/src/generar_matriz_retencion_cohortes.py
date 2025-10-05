import pandas as pd
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '..', 'data', 'data.csv')

try:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta: {file_path}")
    exit()

df.dropna(subset=['CustomerID'], inplace=True)
df['CustomerID'] = df['CustomerID'].astype(int)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df_net = df[~df['InvoiceNo'].astype(str).str.contains('C', na=False)].copy()

def get_month(date):
    return date.strftime('%Y-%m')

df_net['TransactionMonth'] = df_net['InvoiceDate'].apply(get_month)
df_cohorts = df_net.groupby('CustomerID')['InvoiceDate'].min().reset_index()
df_cohorts.rename(columns={'InvoiceDate': 'AcquisitionDate'}, inplace=True)
df_cohorts['CohortMonth'] = df_cohorts['AcquisitionDate'].apply(get_month)
df_merged = pd.merge(df_net, df_cohorts[['CustomerID', 'CohortMonth', 'AcquisitionDate']], on='CustomerID', how='left')

def get_date_int(df, column):
    year = df[column].dt.year
    month = df[column].dt.month
    return year, month

transaction_year, transaction_month = get_date_int(df_merged, 'InvoiceDate')
cohort_year, cohort_month = get_date_int(df_merged, 'AcquisitionDate')

df_merged['MonthIndex'] = (transaction_year - cohort_year) * 12 + \
                          (transaction_month - cohort_month)

cohort_counts = df_merged.groupby(['CohortMonth', 'MonthIndex'])['CustomerID'].nunique().reset_index()
cohort_matrix = cohort_counts.pivot_table(index='CohortMonth',
                                          columns='MonthIndex',
                                          values='CustomerID')
cohort_sizes = cohort_matrix.iloc[:, 0]

retention_matrix = cohort_matrix.div(cohort_sizes, axis=0)
retention_matrix_percent = retention_matrix.mul(100).round(2)

deliverables_path = os.path.join(script_dir, '..', 'deliverables', 'cohort_retention_matrix.csv')

retention_matrix_percent.to_csv(deliverables_path, index=True)

print("\n--- ÉXITO: ANÁLISIS DE COHORTES COMPLETADO ---")
print("Matriz de Retención guardada en:\n", deliverables_path)
print("\nMatriz de Retención (%):")
print(retention_matrix_percent)