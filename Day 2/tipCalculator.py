print("Welcome to the tip calculator!")
total_of_bill = float(input("What was the total bill? \n$"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
number_of_people = int(input("How many people to split the bill? \n"))

tip_amount = total_of_bill * (tip_percentage * 0.01)
total_amount = total_of_bill + tip_amount

print("Each person should pay: $" + str(round(total_amount / number_of_people, 2)))
