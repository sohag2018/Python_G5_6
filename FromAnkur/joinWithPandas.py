# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("sohag.csv")
#print(data)

#print("After droping-------------------------")
# dropping null value columns to avoid errors
#data.dropna(inplace=True)
# print(data)

#(1)
# print("After joining-------------------------")
# # joining string and overwriting
# data['Name'] = data['Name'].str.join("-")
# print(data)

# (2)Joining elements of a list
# splitting string and overwriting
data["Team"] = data["Team"].str.split("")
print(data)
print("------------")
# joining with "_"
data["Team"] = data["Team"].str.join("_")

# display
print(data)
