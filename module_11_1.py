# В PyCharm не работал Matplotlib и Pandas иногда ругался, поэтому делал в VSCode

import requests
import pandas as pd
import matplotlib.pyplot as plt

# 1. Используем библиотеку requests для получения данных с сайта
def take_data():
    url = "https://jsonplaceholder.typicode.com/posts"  # Пример API
    response = requests.get(url)  # Запрос данных
    if response.status_code == 200:
        data = response.json()  # Преобразуем в JSON
        print("Успешно получили данные!")
        return data
    else:
        print("Ошибка при запросе данных")
        return []

# 2. Используем pandas для простого анализа данных
def analyze_data(data):
    df = pd.DataFrame(data)  # Преобразуем данные в таблицу pandas
    print("\nПример данных:")
    print(df.head(3))  # Показываем первые 3 строки таблицы

    user_counts = df['userId'].value_counts()  # Подсчитываем записи на пользователя
    print("\nКоличество записей на каждого пользователя:")
    print(user_counts)

    return user_counts

# 3. Используем matplotlib для построения простого графика
def visualize_data(user_counts):
    user_counts.plot(kind='bar', color='lightblue')  # Строим график
    plt.title("Количество записей на пользователя")
    plt.xlabel("User ID")
    plt.ylabel("Количество записей")
    plt.show()

# Основная часть программы
if __name__ == "__main__":
    data = take_data()  # Получаем данные
    if data:
        user_counts = analyze_data(data)  # Анализируем данные
        visualize_data(user_counts)  # Визуализируем результат
