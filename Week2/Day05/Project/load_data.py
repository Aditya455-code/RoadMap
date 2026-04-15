from sqlalchemy import create_engine
import pandas as pd

# MySQL connection string
engine = create_engine("mysql+pymysql://root:Learning%40841@localhost:3306/sales_db")

df = pd.read_csv("sales_data.csv")

df.to_sql("sales", engine, if_exists="replace", index=False)

print("Data loaded into database!")