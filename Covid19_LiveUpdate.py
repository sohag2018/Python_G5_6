# find chainas covid status
import pandas as pd
covid_data = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-13-2020.csv")
#Entire Data
#print(covid_data)
print("***************************")
print("***** COVID-19 UPDATE *****")
print("***************************")
class Search():
    def result(self):
        selectCountry=input(print("Enter the country Name:"))
        result = covid_data[covid_data['Country_Region'] == selectCountry]  #Entire [Country] data:
    #print(c_data)

    #With selected column:
       # c_data = c_data[['Province_State', 'Confirmed', 'Deaths', 'Recovered']]
    #print(c_data)

    #Sorting:
       # sortedData = c_data.sort_values(by='Confirmed', ascending=False) # for ascending make ascending=True
    #print(sortedData)

    #Reseting:
        #result = sortedData.reset_index(drop=False)
        tD=result["Deaths"].sum()
        tR=result["Recovered"].sum()
        tC=result["Confirmed"].sum()

        print('''Enter What you want to see. 
        Enter 1 for Total Death
        Enter 2 for Total Recovered
        Enter 3 for Total Case
        or Enter 4 for all of above''')

        for i in range(1):
            userInput=input(print("\nPlease Enter 1/ 2 /3 /4:"))
            if userInput=="1":
                print(f"In {selectCountry} Total Death:",tD)
            elif userInput=="2":
                print(f"In {selectCountry} Total Recovered:",tR)
            elif userInput=="3":
                print(f"In {selectCountry} Total Case:",tC)
            elif userInput=="4":
                print(f"In {selectCountry} Total Death:{tD}, Recovered:{tR}, Case:{tC}")

        furtherSearch = input(print("""\nContinue to search? 
        Enter 1 for yes & 2 for no"""))
        if furtherSearch == "1":
            s1.result()

        else:
            print("""**************************
**** THANKS FOR USING ****
**** COVID-19 UPDATE  **** 
**************************""")

s1=Search()
s1.result()

