import pandas as pd

data = {"calories": [45, 78, 110, 120],
      "Day": ["Day1", "Day2", "Day3", "Day4"],
      "Month": ["Jan", "Feb", "March", "Apr"]
      }

print(data)
df = pd.DataFrame(data)
print(df)
