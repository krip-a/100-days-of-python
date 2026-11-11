import pandas 


data = pandas.read_csv("./weather/weather_data.csv")    #returns a dataframe
#print(type(data)
#type(data["temp"])         gonan be a Series

#data_dict = data.to_dict()                              #convert each column to a dictionary
#temp_list = data["temp"].to_list()                      #convert specified row to list

#avg_temp =sum(temp_list) / len(temp_list)
#print(avg_temp)

#print(data["temp"].mean())      #find mean of the given column
#print(data["temp"].max())       #find the max of the given column

#get data in columns
#data["temp"]                    
#data["condition"]
#or
#print(data.condition)

#get data in rows
#print(data[data.day == "Monday"])

#print the row w highest temp
#print(data[data.temp == data["temp"].max()])

#get specific column from a speific row
#monday = data[data.day == "Monday"]
#print(monday.condition)

#convert monday's temp to farenheit
#f_temp = data[data.day == "Monday"].temp[0]
#c_temp = (f_temp * (9/5)) + 32
#print(c_temp)

#creating a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./weather/new_csv.csv")
print(df)