import json
import urllib.request

def get_weather_data(city):
    api_key = "b6907d289e10d714a6e88b30761fae22"
    base_url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid={api_key}"
    with urllib.request.urlopen(base_url) as response:
        data = json.loads(response.read().decode())
    return data

def get_temperature_by_date(data, date):
    for forecast in data['list']:
        if forecast['dt_txt'] == date:
            return forecast['main']['temp']
    return None

def get_wind_speed_by_date(data, date):
    for forecast in data['list']:
        if forecast['dt_txt'] == date:
            return forecast['wind']['speed']
    return None

def get_pressure_by_date(data, date):
    for forecast in data['list']:
        if forecast['dt_txt'] == date:
            return forecast['main']['pressure']
    return None

def main():
    city = "London,us"
    weather_data = get_weather_data(city)

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature_by_date(weather_data, date)
            if temperature:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("Invalid date or data not available.")

        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Invalid date or data not available.")

        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Invalid date or data not available.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
