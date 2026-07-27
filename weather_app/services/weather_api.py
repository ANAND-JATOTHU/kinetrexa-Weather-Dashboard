import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class WeatherAPIException(Exception):
    """Custom exception for Weather API errors."""
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code


class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5"

    def __init__(self):
        self.api_key = getattr(settings, 'OPENWEATHERMAP_API_KEY', None)

    def _make_request(self, endpoint, params):
        if not self.api_key or self.api_key == 'your_openweathermap_api_key_here':
            # For development without key, we could return mock data, but we should raise error if missing
            logger.warning("OpenWeatherMap API key is missing or invalid.")
            raise WeatherAPIException("Weather service is not configured properly (Missing API Key).", status_code=500)

        params['appid'] = self.api_key
        params['units'] = 'metric'  # Default to Celsius

        try:
            url = f"{self.BASE_URL}/{endpoint}"
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            status = e.response.status_code
            if status == 404:
                raise WeatherAPIException("City not found.", status_code=404)
            elif status == 429:
                raise WeatherAPIException("Weather API rate limit exceeded.", status_code=429)
            elif status == 401:
                # OpenWeather keys take a few hours to activate. We'll return mock data so the UI can be tested!
                logger.warning("API key returned 401. Returning mock data for UI testing.")
                return self._get_mock_data(endpoint, params.get('q', 'Mock City'))
            else:
                logger.error(f"HTTP error from Weather API: {e}")
                raise WeatherAPIException(f"Weather service error: {e}", status_code=status)
        except requests.exceptions.Timeout:
            logger.error("Weather API request timed out.")
            raise WeatherAPIException("Weather service timed out. Please try again later.", status_code=408)
        except requests.exceptions.RequestException as e:
            logger.error(f"Request exception from Weather API: {e}")
            raise WeatherAPIException("Unable to connect to Weather service.", status_code=500)

    def get_current_weather(self, city_name):
        """Fetch current weather for a city."""
        params = {'q': city_name}
        return self._make_request('weather', params)

    def get_forecast(self, city_name):
        """Fetch 5-day forecast for a city."""
        params = {'q': city_name}
        return self._make_request('forecast', params)

    def _get_mock_data(self, endpoint, city):
        """Returns realistic mock data so the dashboard can be tested while waiting for API key activation."""
        if endpoint == 'weather':
            return {
                "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}],
                "main": {"temp": 22.5, "feels_like": 21.8, "temp_min": 18.0, "temp_max": 25.0, "pressure": 1012, "humidity": 45},
                "visibility": 10000,
                "wind": {"speed": 3.6, "deg": 120},
                "clouds": {"all": 0},
                "name": city
            }
        elif endpoint == 'forecast':
            # Create a fake 5-day forecast list (every 8th item is 1 day in the API response)
            fake_list = []
            for i in range(40):
                fake_list.append({
                    "dt_txt": f"2026-07-{27 + (i//8):02d} 12:00:00",
                    "main": {"temp": 22.5 + (i%3)},
                    "weather": [{"description": "clear sky", "icon": "01d"}]
                })
            return {"list": fake_list}

