# Weather App

The Weather App is a simple Django web application that allows users to retrieve current weather information for a specific city.

## Features

- Display current weather conditions including temperature, description, and icon.
- Retrieve weather data using the OpenWeatherMap API.
- Search for weather information by entering a city name.

## Technologies Used

- Python
- Django
- HTML
- CSS
- OpenWeatherMap API

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/natzsmart/WeatherApp.git
   ```

2. Change to the project directory:

   ```
   cd weather-app
   ```

3. Create and activate a virtual environment:

   ```
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Set up the API key:

   - Open the `config.py` file and replace `'your-api-key'` with your OpenWeatherMap API key.

6. Run the application:

   ```
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

- Enter a city name in the search input to retrieve the current weather information for that city.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The Weather App utilizes the OpenWeatherMap API to retrieve weather data. Visit [OpenWeatherMap](https://openweathermap.org/) for more information.
