import requests
import keyboard
import sys
API_KEY = 'def391ad2fdda854f505476ff9c2395e'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'



def start():
    
    print('Welcome to the weather application. ')
    city = input('Enter the city name: ')
    request_url = f'{BASE_URL}?q={city}&appid={API_KEY}'
    response = requests.get(request_url)
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15)

    print(f'Weather in {city} is {temperature} degrees Celsius with {weather}')

def menu():
    while True:
        choice = input('If you wish to continue with another city press 1 , or just close application with 2.' )
        
        if choice == '1':
            start()
        elif choice == '2':
            sys.exit(0)
            
        else:
            print('Incorrect keyword')

start()
menu()
