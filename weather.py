import requests

API_KEY = 'def391ad2fdda854f505476ff9c2395e'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city name: ')
request_url = f'{BASE_URL}?q={city}&appid={API_KEY}'
response = requests.get(request_url)
data = response.json()
weather = data['weather'][0]['description']
temperature = round(data['main']['temp'] - 273.15)


print(f'Weather in {city} is {temperature} degrees celsius with {weather}')









