import pandas as pd
import matplotlib.pyplot as plt
ipl = pd.read_csv('F:\\PythonProject\\Drivers\\matches.csv')
df = pd.DataFrame(ipl)

print(df.head())

print(df.columns)

print(df[['team1', 'team2']])

print(df[['team1', 'team2', 'winner']])

print(df['winner'].value_counts())

df['winner'].value_counts(normalize=True).plot(kind='bar')
plt.show()

print(df['venue'].value_counts())
df['venue'].value_counts(normalize=True).plot(kind='bar')
plt.show()

print(df.columns)

print(df['player_of_match'].value_counts().head(5))
df['player_of_match'].value_counts(normalize=True).head(5).plot(kind='pie')
plt.show()

# umpire
print(df['umpire1'].value_counts().head(5))
df['umpire1'].value_counts(normalize=True).head(5).plot(kind='pie')
plt.show()

# umpire
print(df['umpire2'].value_counts().head(5))
df['umpire2'].value_counts(normalize=True).head(5).plot(kind='pie')
plt.show()

# umpire
print(df['umpire3'].value_counts().head(5))
df['umpire3'].value_counts(normalize=True).head(5).plot(kind='pie')
plt.show()

#Null treatment
print(df.isna())