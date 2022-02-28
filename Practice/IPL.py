import pandas as pd
ipl = pd.read_csv('F:\\PythonProject\\Drivers\\matches.csv')
df = pd.DataFrame(ipl)
print(df.head())
print(df.columns)
print(df[['team1', 'team2']])