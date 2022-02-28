import pandas as pd
import numpy as np
data = {"calories": [45, 78, 110, 120],
      "Day": ["Day1", "Day2", "Day3", "Day4"],
      "Month": ["Jan", "Feb", "March", "Apr"]
      }

print(data)
df = pd.DataFrame(data)
print(df)

arr = np.arange(1, 10)
print(arr)
print(arr.shape)
arr = arr.reshape(3, 3)
print(arr)
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(iris)

