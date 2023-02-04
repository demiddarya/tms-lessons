# Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
# Если он ответил “yes” - завершите программу.
# Если он ответил “no” - продолжайте - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you"
# и продолжайте спрашивать до тех пор, пока ответ не будет корректным.

for i in range(0, 100):
    answer = input('Should we break?')
    if answer == 'yes':
        break
    elif answer == 'no':
        print(i)
        continue
    else:
        print("Don't understand you")
        continue
