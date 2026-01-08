import pandas as pd

df = pd.read_parquet(r"D:\GitLocal\big_data\Databricks\databricks-masterclass\data\shoppinginvoices\invoices_1_100.parquet")
print(df.head())        # first 5 rows
print(df.info())        # schema




