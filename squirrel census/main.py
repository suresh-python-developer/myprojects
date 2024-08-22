import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240803.csv")
gray_colour = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_colour = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_colour = len(data[data["Primary Fur Color"] == "Black"])
print(gray_colour)
print(cinnamon_colour)
print(black_colour)

data_dic = {
    "color" : ["gray","cinnamon","black" ],
    "count"  : [gray_colour,cinnamon_colour,black_colour]
}
df = pandas.DataFrame(data_dic)
