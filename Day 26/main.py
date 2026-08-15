import random

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# doubled_nums = [n * 2 for n in range(1, 5)]
# print(doubled_nums)

names = ["Alex", "Beth", "Charlie", "Daniel", "Elizabeth", "Fran", "Grof"]
# # short_names = [name for name in names if len(name) <= 4]
# # print(short_names)
# long_names = [name.upper() for name in names if len(name) >= 5]
# print(long_names)
student_scores = {student:random.randint(1,100) for student in names}
passed_students = {key:value for (key, value) in student_scores.items() if value >= 75}
print(student_scores)
print(passed_students)
