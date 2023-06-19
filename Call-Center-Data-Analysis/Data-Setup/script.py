import pandas as pd

def month_name(d):
    if d==1 : return "January"
    elif d==2 : return "February"
    if d==3 : return "March"
    elif d==4 : return "April"
    if d==5 : return "May"
    elif d==6 : return "June"
    if d==7 : return "July"
    elif d==8 : return "August"
    if d==9 : return "September"
    elif d==10 : return "October"
    if d==11 : return "November"
    elif d==12 : return "December"
    else : return "None"

files_data = []

# Reading all data-files and storing required content into a list
for i in range(11,23):
    file_name = "Calls_for_Service_20{}.csv".format(i) # make sure to put all data-files in same directory as of script.py
    print("Reading {}.....".format(file_name))
    file = pd.read_csv(file_name)
    df = file[['TypeText','TimeCreate']]
    files_data.append(df)

# concatenating all dataframes stored in list
collective_data = pd.concat(files_data)

# extracting date from time-create, then extracting month & year out of that and store them in individual columns
print("Necessary pre-processing, it will take some time.......")
collective_data["Date"] = pd.to_datetime(collective_data.TimeCreate)
collective_data["Month"] = collective_data.Date.apply(lambda x:x.month).apply(month_name)
collective_data["Year"] = collective_data.Date.apply(lambda x:x.year)

# dropping-off un-necessary data columns
collective_data.drop(["TimeCreate","Date"],axis=1,inplace=True)

# saving data in same directory
collective_data.to_csv("Calls_Data.csv",index=False)
print("Data saved successfully!")