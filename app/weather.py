import os

import aiohttp
from dotenv import load_dotenv

load_dotenv()


async def fetch_weather(city: str):
    api_key = os.getenv('WEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather_data = await response.json()
            if 'main' not in weather_data:
                raise ValueError(f"City {city} not found")
            # Преобразуем в градусы по Цельсию
            temperature = int(weather_data['main']['temp']) - 273.15
            return temperature
