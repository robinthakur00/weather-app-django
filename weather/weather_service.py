import requests

def get_weather(city):
   api_key = '0c36e377f8cd4fa28f4155436231204'  # Replace with your provided API key

   url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
   response = requests.get(url)
   
   if response.status_code == 200:
       data = response.json()
       temp_c = data['current']['temp_c']
       condition = data['current']['condition']['text']
       wind_kph = data['current']['wind_kph']
       humidity = data['current']['humidity']

       return {
           'temp_c': temp_c,
           'condition': condition,
           'wind_kph': wind_kph,
           'humidity': humidity
       }

   return None
