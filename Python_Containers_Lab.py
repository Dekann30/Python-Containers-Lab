# Exercise 1
students = ['Deanna', 'Nathan', 'Germano', 'Joan', 'Ashley', 'Ramon']
print(students[1])
print(students[-1])

# Exercise 2
foods = ('pizza', 'chips', 'nachos', 'spicy pork', 'tacos', 'curry')

for food in foods:
    print(f'{food} is good food.')

# Exercise 3
for food in foods:
    if foods[len(foods)-1] == food or foods[len(foods)-2] == food:
        print(food)

# Exercise 4
home_town = {
    "city": "Columbus",
    "state": "Ohio",
    "population": "889,079"
}
print(f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')

# Exercise 5
for key, value in home_town.items():
    print(f'{key} = {value}')

# Exercise 6
cohort = []

leng = 0
for idx, student in enumerate(students):
    dict = {}
    dict['student'] = student
    dict['fav_food'] = foods[idx]
    cohort.append(dict)

for index in cohort:
    print(index)


# Exercise 7
awesome_students = [f'{student} is awesome!' for student in students]

for idx, student in enumerate(awesome_students):
    print(student)

# Exercise 8
a = [food for food in foods if 'a' in food]
print(a)