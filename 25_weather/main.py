#
# # with open ("weather_data.csv", mode = "r") as weather:
# #     data = weather.readlines()
# #
# # print (data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append( int(row[1]) )
# #
# # print (temperatures)
#
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# temp_list = (data["temp"]).to_list()
# total_temp = sum(temp_list)
# count_temp = len(temp_list)
# avg_temp = total_temp / count_temp
# print (avg_temp)
#
#
# # print (data["temp"].mean())
# #
# # print (data["temp"].max())
# #
# # print (data.condition)
#
# # you can pull the data where the day is monday
# print (data[data.day == 'Monday'])
#
# # you can pull the data with the equivalent of a subquery
# print (data[data.temp == data.temp.max()])
#
# # you can also specify just certain things.
# print (data.day[data.temp == data.temp.max()])
#
#
# # Create a dataframe from scratch.
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 86]
# }
#
# new_data_frame = pandas.DataFrame(data_dict)
# # And you can export into a csv
# new_data_frame.to_csv("new_data_frame.csv")
#


import pandas
data = pandas.read_csv("squirrel_data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur_Color":["Gray","Cinnamon","Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

