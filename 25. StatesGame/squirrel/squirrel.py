import pandas as pd

df = pd.read_csv("./squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colors = df["Primary Fur Color"].unique()

gray = len(df[df["Primary Fur Color"] == "Gray"])
black = len(df[df["Primary Fur Color"] == "Black"])
cinnamon = len(df[df["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["gray", "black", "cinnamon"],
    "count": [gray, black, cinnamon]
}
new_df = pd.DataFrame(data_dict)
new_df.to_csv("./squirrel/squirrel_count.csv")
