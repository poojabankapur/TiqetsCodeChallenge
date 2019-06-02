# Databricks notebook source
import pandas as pd
barcodes = pd.read_csv("/dbfs/FileStore/tables/barcodes.csv").drop_duplicates(subset='barcode', keep="first")
orders = pd.read_csv("/dbfs/FileStore/tables/orders.csv")
joined = orders.join(barcodes.set_index('order_id'),on='order_id',how='inner')
grouped = joined.groupby(['customer_id','order_id'])['barcode'].apply(list)
grouped

# COMMAND ----------


