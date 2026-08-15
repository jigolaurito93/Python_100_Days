# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# doubled_nums = [n * 2 for n in range(1, 5)]
# print(doubled_nums)

names = ["Alex", "Beth", "Charlie", "Daniel", "Elizabeth", "Fran", "Grof"]
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)