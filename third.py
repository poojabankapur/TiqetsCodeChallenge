import pandas as pd
barcodes = pd.read_csv("/dbfs/FileStore/tables/barcodes.csv")
barcodes['order_id'].isnull().sum()
