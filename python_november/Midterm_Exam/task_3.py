# Запрашиваем у пользователя число

number_1 = int(input("Введите число 1: "))
number_2 = int(input("Введите число 2: "))
number_3 = int(input("Введите число 3: "))

# Сравниваем ввденные числа

if number_1 > number_2 and number_1 > number_3:
    print("Наибольшее число 1: ", number_1)
elif number_2 > number_3:
    print("Наибольшее число 2: ", number_2)
else:
    print("Наибольшее число 3: ", number_3)



