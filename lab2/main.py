print("Задание 1:")
import numpy as np
import time
# Реализация собственной функции matmul
def matmul(a: object, b: object) -> object:
    result = np.zeros((a.shape[0], b.shape[1]))
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            for k in range(a.shape[1]):
                result[i, j] += a[i, k] * b[k, j]
    return result

a = np.random.rand(200, 300)
b = np.random.rand(300, 200)

start_time = time.time()
ab = np.matmul(a, b)
elapsed_time_ab = time.time() - start_time
print(f"Время выполнения np.matmul: {elapsed_time_ab} секунд")

start_time = time.time()
ab_custom = matmul(a, b)
elapsed_time_ab_custom = time.time() - start_time
print(f"Время выполнения собственной функции matmul: {elapsed_time_ab_custom} секунд")

# Сравнение результатов и скорости работы
print("Сравнение результатов:")

if np.allclose(ab_custom, ab):
    print("Результаты совпадают.")
else:
    print("Результаты не совпадают.")

print("Сравнение скорости работы:")

if elapsed_time_ab < elapsed_time_ab_custom :
    print("Функция np.matmul работает быстрее ")
elif elapsed_time_ab > elapsed_time_ab_custom :
    print("Функция matmul работает быстрее ")
else:
    print("Скрость работы совпадают")
print("___________________________________")
print("Задание 2:")



a = np.random.rand(9001)

# С помощью логической индексации
start_time = time.time()
count_a = np.sum(a > 0.5)
sum_a = np.sum(a[a > 0.5])
elapsed_time_logical_indexing = time.time() - start_time

# С помощью цикла for
count_a_for = 0
sum_a_for = 0
start_time = time.time()
for element in a:
    if element > 0.5:
        count_a_for += 1
        sum_a_for += element
elapsed_time_for_loop = time.time() - start_time

print(f"С использованием логической индексации: Количество={count_a}, Сумма={sum_a}")
print(f"С использованием цикла for: Количество={count_a_for}, Сумма={sum_a_for}")

print(f"Время выполнения с логической индексацией: {elapsed_time_logical_indexing} секунд")
print(f"Время выполнения с циклом for: {elapsed_time_for_loop} секунд")
print("___________________________________")
print("Задание 3:")

import pandas as pd

df = pd.read_csv('C:\\Users\\Nastassija_8\\OneDrive\\Рабочий стол\\olympics.csv', index_col=0, skiprows=1)



for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

# Страна с наибольшим количеством золотых медалей на летних ОИ
summer_gold_max = df['Gold'].idxmax()
print("Страна с наибольшим количеством золотых медалей на летних ОИ:", summer_gold_max)

# Страна с наибольшей разницой в количестве наград на летних и зимних ОИ
df['Difference'] = abs(df['Total'] - df['Total.1'])
max_difference_country = df['Difference'].idxmax()
print("Страна с наибольшей разницой в количестве наград на летних и зимних ОИ:", max_difference_country)

# Cтрана имеет наибольшую разницу в количестве золотых медалей на летних и зимних ОИ по отношению к общему количеству золотых медалей для данной страны
df = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)]
df['Gold Difference Ratio'] = (df['Gold'] - df['Gold.1']) / df['Gold.2']
max_difference_ratio = df['Gold Difference Ratio'].idxmax()
print("Страна с наибольшей разницой в количестве золотых медалей на летних и зимних ОИ по отношению к общему количеству золотых медалей для данной страны:", max_difference_ratio)

print("Создание Series 'Points'")

points = df['Gold'] * 3 + df['Silver'] * 2 + df['Bronze']
points_series = pd.Series(points, name='Points')
print(points_series)

print("___________________________________")
print("Задание 4:")

df = pd.read_csv('C:\\Users\\Nastassija_8\\OneDrive\\Рабочий стол\\census.csv')

# Количество графств в каждом штате
county_counts = df['STNAME'].value_counts()
state_with_most_counties = county_counts.idxmax()
print(f"Штат с наибольшим количеством графств: {state_with_most_counties}")

# Общее население графств
df['Total Population'] = df['CENSUS2010POP'] + df['ESTIMATESBASE2010'] + df['POPESTIMATE2011'] + df['POPESTIMATE2012'] + df['POPESTIMATE2013'] + df['POPESTIMATE2014'] + df['POPESTIMATE2015']

# Общее население для каждого штата
state_populations = df.groupby('STNAME')['Total Population'].sum()
top_3_states = state_populations.sort_values(ascending=False).head(3)
print(top_3_states)

# Вычисление разницы между максимальной и минимальной численностью населения за 5 лет
df['PopulationChange'] = df[['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']].max(axis=1) - df[['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']].min(axis=1)

# Графство с максимальным изменением численности населения
max_population_change_county = df.loc[df['PopulationChange'].idxmax()]['CTYNAME']

print("Графство с самым крупным изменением численности населения в период 2010-2015:", max_population_change_county)

# Выберем графства из регионов 1 и 2, чье название начинается с 'Washington' и условие по численности населения
selected_counties = df[(df['REGION'].isin([1, 2])) & (df['CTYNAME'].str.startswith('Washington')) & (df['POPESTIMATE2015'] > df['POPESTIMATE2014'])]

# Выведем результат
print("Графства из регионов 1 или 2, начинающиеся с 'Washington', с POPESTIMATE2015 > POPESTIMATE2014:")
print(selected_counties)

