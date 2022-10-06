import pandas as pd

CSV_PATH = "supermarket_sales.csv"
df = pd.read_csv(CSV_PATH, sep=',')

print(df)