# This program will be used to find how many pizza slices and pies are needed for a certain amount of students.
# 2/17/2022
# CTI-110 P1HW2 - Pizza Order
# Kai Olivencia

students = int(input('How many students do you want to order pizza for? '))

print('Pizza Order')

print('Number of students: ', students)

slices = students * 3

pies = slices / 6

print('Pizza slices needed: ', slices)

print('Pizzas needed: ', pies)
