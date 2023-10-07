# This is a sample Python script.

print("Задание 1:")


def fibonacci(n):
    if n <= 0:
        print("n должно быть положительным целым числом.")
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        result = 0
        for i in range(3, n + 1):
            result = a + b
            a, b = b, result
        return result


print(fibonacci(10))

print("Задание 2:")
def is_divisible(a, b, verbose=False):
    if verbose:
        print("Начало проверки:")
    if b == 0:
        print("Делитель (b) не может быть равен нулю.")
        return
    remainder = a % b
    if remainder == 0:
        return True
    else:
        return False
print(is_divisible(100, 5, True))
print(is_divisible(100, 2, True))
print(is_divisible(10, 0, True))

print("Задание 3:")

list_of_numbers = list(range(99))
list_of_strings = [str(number) for number in list_of_numbers]

print(list_of_strings)

print("Задание 4:")

mixed_list = [1, "2", 3, "4", 5, "6", 7, "8", 9, "10"]

number_list = []
string_list = []

for item in mixed_list:
    if isinstance(item, int):
        number_list.append(item)
    elif isinstance(item, str):
        string_list.append(item)

print("Список чисел (number_list):", number_list)
print("Список строк (string_list):", string_list)

print("Задача 8_4:")

# Используем list comprehension для создания списка чисел (number_list)
number_list_ = [x for x in mixed_list if isinstance(x, (int, float))]

# Используем list comprehension для создания списка строк (string_list)
string_list_ = [x for x in mixed_list if isinstance(x, str)]

print("Список чисел (number_list):", number_list_)
print("Список строк (string_list):", string_list_)

print("Задание 5:")

import statistics

sales_per_month = {
    'Jannuary': 50,
    'February': 100,
    'March': 42,
    'April':87,
    'May':500,
    'June':128,
    'July':101,
    'August':78,
    'September':121,
    'October':91,
    'November':89,
    'December':190
}

max_value = None
min_value = None
max_value_key = None
min_value_key = None
anomalous_keys = []


# Вычисляем среднее значение
mean_value = statistics.mean(sales_per_month.values())

# Вычисляем дисперсию
variance = statistics.variance(sales_per_month.values())

for key, value in sales_per_month.items():
    # Поиск максимального значения и ключа
    if max_value is None or value > max_value:
        max_value = value
        max_value_key = key

    # Поиск минимального значения и ключа
    if min_value is None or value < min_value:
        min_value = value
        min_value_key = key

    # Проверяем на аномалии
    if abs(value - mean_value) > 2 * variance:
        anomalous_keys.append(key)
print("Среднее значение:", mean_value)
print("Дисперсия:", variance)
print("Аномальные ключи:", anomalous_keys)
print("Максимальное значение и ключ:", max_value_key, max_value)
print("Минимальное значение и ключ:", min_value_key, min_value)


print("Задача 8_5:")

# Находим максимальное и минимальное значение

max_value_key_ = max(sales_per_month, key=sales_per_month.get)
min_value_key_ = min(sales_per_month, key=sales_per_month.get)

# Используем list comprehension определяем аномальные значения
anomalous_keys_ = [key for key, value in sales_per_month.items() if abs(value - mean_value) > 2 * variance]

print("Среднее значение:", mean_value)
print("Дисперсия:", variance)
print("Аномальные ключи:", anomalous_keys_)
print("Максимальное значение и ключ:", max_value_key_, sales_per_month[max_value_key_])
print("Минимальное значение и ключ:", min_value_key_, sales_per_month[min_value_key_])

print("Задание 6:")

from datetime import datetime, timedelta

# Дата дня рождения одногруппника
birthdays = [
    datetime(year=2023, month=12, day=15),
    datetime(year=2023, month=11, day=20),
    datetime(year=2023, month=12, day=5)
]

# Текущая дата
today = datetime.today()

min_days_difference = float('inf')

# Перебираем все даты дней рождения и находим ближайшую
for birthday in birthdays:
    difference = (birthday - today).days
    if 0 <= difference < min_days_difference:
        min_days_difference = difference
        closest_birthday = birthday

print("Ближайший день рождения одногруппника:", closest_birthday.strftime("%d.%m.%Y"))
print("Осталось дней до ближайшего дня рождения:", min_days_difference)

print("Задача 8_6:")
# Используем list comprehension для расчета разницы между текущей датой и днями рождения
differences = [abs((birthday - today).days) for birthday in birthdays]

# Находим ближайшую дату
closest_index = differences.index(min(differences))

# Получаем ближайший день рождения
closest_birthday = birthdays[closest_index]

# Количество дней до ближайшего дня рождения
days_until_next_birthday = (closest_birthday - today).days

print("Ближайший день рождения одногруппника:", closest_birthday.strftime("%d.%m.%Y"))
print("Осталось дней до ближайшего дня рождения:", days_until_next_birthday)

print("Задание 7:")
mixed_list = [1, 2.5, 3, 4.5, 5.0]

result_list = list(map(lambda x: int(x) ** 4, mixed_list))
print(result_list)
print("Задание 8_7:")
result = [int(x) ** 4 for x in mixed_list]
print(result)