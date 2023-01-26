#Напишите программу, которая спрашивает у пользователя как его зовут,
#затем какого он года рождения. После этого программа выводит
#Hello {name}. Your age is {age}.

print('what is your name?')
user_name = input()
print('What is your birth year?')
user_year = input()
user_age: int = 2023 - int(user_year)
print('Hello ' + user_name + '. ' + 'Your age is ' + str(user_age) + '.')
