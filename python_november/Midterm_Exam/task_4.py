# Создаем список кортеджей
students = [('Анна', 23), ('Рустам', 36), ('Адам', 24), ('Амина', 26)]


# Извлекаем имена и возраста и списка
names = [name for name, age in students]
ages = [age for name, age in students]

# Вывод имен и возраста
print(f'Имена: {names}')
print(f'Возраста: {ages}')
