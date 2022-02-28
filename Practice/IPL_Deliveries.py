import pandas as pd
deli = pd.read_csv('F:\\PythonProject\\Drivers\\deliveries.csv')

df1=pd.DataFrame(deli)

# Column of dataset
print(df1.columns)
