# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DeepSkyBlue4")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# print(timmy)

from prettytable import PrettyTable

# table = PrettyTable()
table2 = PrettyTable()

resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
resources_name = []
resources_amount = []
for item in resources:
    resources_name.append(item)
    resources_amount.append(resources[item])
print(resources_name, resources_amount)

table2.add_column("Ingredient", resources_name)
table2.add_column("Amount", resources_amount)

print(table2)


# table.add_column("City Name", ["Adelaide", "Brisbane", "Darwin", "Hobart", "Sydney", "Melbourne", "Perth"])
# table.add_column("Population", [1295, 1209, 1357, 2058, 4336, 4619, 1554])
# table.align = "l"
# print(table)