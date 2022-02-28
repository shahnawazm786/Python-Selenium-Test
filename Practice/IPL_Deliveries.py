import pandas as pd
deli = pd.read_csv('F:\\PythonProject\\Drivers\\deliveries.csv')

df1=pd.DataFrame(deli)

# Column of dataset
print(df1.columns)

print(df1.head(5))

# Show the fielder who dismiss the batsman
print(df1['fielder'].head(10))

# show the dismissal_kind

print(df1['dismissal_kind'])