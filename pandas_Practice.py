# From the given dataset print the first and last five rows
import pandas as pd
import numpy

# Python dict object
student_dict = {'Name': ['Joe', 'Nat'], 'Age': [20, 21], 'Marks': [85.10, 77.80]}
print(student_dict)

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)
cars = pd.read_csv("Automobile_data.csv")
print(cars)
student_df.info()
student_df.describe()