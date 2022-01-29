import requests

def try_me():

    url = "https://www.metaweather.com/api/location/44418/"
    response = requests.get(url).json()
    weather = response["consolidated_weather"][0]["weather_state_name"]

    return f'The weather at Le Wagon today is: {weather}'


if __name__ == "__main__":
    print(try_me())
