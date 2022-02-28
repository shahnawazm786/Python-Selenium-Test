import pandas as pd
ipl = pd.read_csv('Drivers/matches.csv')
df = pd.DataFrame(ipl)
print(df.head())