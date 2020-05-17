#Python Dates-->is not a data type of its own
import datetime

print("\n## type-----------------------------------")
print(datetime.date)  # <class 'datetime.date'>

print("\n## display current date&time---------------")
x=datetime.datetime.now()
print(x)#year, month, day, hour, minute, second, and microsecond
print(x.year)#Current year like 2020
print(x.month)#Cureent Month like 5
print(x.date())#Cureent date like 2020-05-15
print(x.hour)#
print(x.minute)
print(x.second)
print(x.microsecond)

print("\n## display in different form --------------")
#There is a chart (in same dir)-->for specific formats. char in upper or lower and different char represents dif forms
print(x.strftime("%A")) #Friday
print(x.strftime("%a")) #Fri
print(x.strftime("%B")) #May  %b also May
print(x.strftime("%c")) #Fri May 15 17:35:31 2020


print("\n## Creating Date Objects---------------")
'''To create a date, we can use the datetime() class (constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month, day.'''

x = datetime.datetime(2023, 5, 17)
y=datetime.datetime.now()
print("Starting time:",y)

print("diff:",x-y)

print("\n## display the current date---------------")
print("\n## display the current date---------------")
