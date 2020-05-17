import pandas as pd
barcodes = pd.read_csv("/dbfs/FileStore/tables/barcodes.csv")
orders = pd.read_csv("/dbfs/FileStore/tables/orders.csv")
joined = orders.join(barcodes.set_index('order_id'),on='order_id',how='inner')
grouped_data = joined.groupby('customer_id')['barcode'].count()
grouped_data.sort_values(ascending=False).head(5)
