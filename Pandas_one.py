import pandas as pd
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print(pd.__version__)
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])
# Create Labels
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[[0, 1]])
print(pd.options.display.max_rows)
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)
# df = pd.read_json('data.json')
#
# print(df.to_string())
# df = pd.read_csv('data.csv')
print(df.head(3))
print(df.info())
df = pd.read_csv('data.csv')
print(df)
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(df.duplicated())
df.corr()
df.plot()
plt.show()
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()