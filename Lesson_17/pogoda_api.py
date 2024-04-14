import requests

url = 'http://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Los Angeles',
    'appid': ' API_KEY',
    'units': 'metric'
}

response = requests.get(url, params=params)
# Дополнительное задание:
# добавим обработку ошибок в нашем скрипте. Например, если API вернуло ошибку 404,
# выведем соответствующее сообщение
if response.status_code == 404:
    print("Ошибка 404: Ресурс не найден")
elif response.status_code == 500:
    print("Ошибка 500: Внутренняя ошибка сервера")
elif response.status_code == 200:
    data = response.json()
    print(f"Текущая погода в Лос-Анджелесе:")
    print(f"Температура: {data['main']['temp']}°C")
    print(f"Влажность: {data['main']['humidity']}%")
    print(f"Скорость ветра: {data['wind']['speed']} м/c")
else:
    print(f"Ошибка при получении данных. Код ошибки: {response.status_code}")


