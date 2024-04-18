from config import Config
import plugins

import requests
import spacy


nlp = spacy.load('en_core_web_sm')


class WeatherPlugin(plugins.Base):
    def __init__(self):
        self.command = "weather"
        self.aliases = ["the weather", "current weather", "what is it like in"]

    def process(self, text):
        extracted = nlp(text)
        city = ""

        for entity in extracted.ents:
            if entity.label_ == 'GPE':
                city = entity.text
                break
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Config.APIs.OpenWeatherMapAPI}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
                
            return f"The current weather in {city} is {desc} at {round((9/5) * (temp - 273.15) + 32)} fahrenheit."

        else:
            return "I couldn't get the weather data! Try again later."