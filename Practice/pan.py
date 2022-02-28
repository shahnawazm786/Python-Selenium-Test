import pandas as pd
var = pd.Series([23, 24, 25, 26])
print(var)
cal = {"day1": 500, "day2": 400, "day3": 350}
var = pd.Series(cal)
print(var)
print(pd.__version__)
print(type(pd))