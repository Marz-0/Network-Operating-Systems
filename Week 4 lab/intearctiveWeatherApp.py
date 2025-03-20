import socket
import requests

def get_weather_by_city(city):
    api_key = "your_api_key"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"Weather in {city}: {weather_description}, {temperature}°C"
    except requests.exceptions.RequestException as e:
        return handle_api_error(e)

def handle_api_error(e):
    if isinstance(e, KeyError):
        print(f"Key error in API response: {e}")
        return f"API format error: Missing expected data ({e})"
    else:
        print(f"Unexpected error: {e}")
        return f"An error occurred: {e}"

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('localhost', 65433)
        
        print("Interactive Weather App")
        print("Type 'exit' to quit")
        
        while True:
            city = input("Enter city name: ")
            if city.lower() == 'exit':
                break
            
            weather_info = get_weather_by_city(city)
            print(weather_info)
            
            try:
                client_socket.sendto(weather_info.encode(), server_address)
                print("Data sent to server successfully")
            except Exception as e:
                print(f"Error sending data to server: {e}")
                
        client_socket.close()
        
    except Exception as e:
        print(f"Fatal error: {e}")
        print("Press Enter to exit...")
        input()  # This prevents the window from closing immediately

if __name__ == "__main__":
    main()