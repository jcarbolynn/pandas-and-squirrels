import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
  "fur color": ["gray", "cinnamon", "black"],
  "count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
