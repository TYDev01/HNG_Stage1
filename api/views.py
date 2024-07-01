from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from dotenv import load_dotenv
import os


load_dotenv()

@api_view(['GET'])
def newVisitor(request):
    API_KEY = os.getenv("API_KEY")
    WEATHER_API = os.getenv("WEATHER_API")
    visitName = request.query_params.get('visitor_name', 'usersname')


    try:
        get_client_ip = requests.get("https://api.ipgeolocation.io/getip")
        get_client_ip.raise_for_status()
        client_ip = get_client_ip.json().get("ip")
    except requests.RequestException:
        client_ip = "127.0.0.1" #Falls back default ip

    try:
        ipgeo_response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={client_ip}")
        ipgeo_response.raise_for_status()
        client_city = ipgeo_response.json().get('city', 'Unknown')
    except requests.RequestException:
        client_city = "Unknown"

    try:
        weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={client_city}&appid={WEATHER_API}&units=metric')
        weather_response.raise_for_status()
        temperature = weather_response.json().get('main', {}).get('temp', 'Unknown')
    except requests.RequestException:
        temperature = "Unknown"

    data = {
        "client_ip": client_ip,
        "location": client_city,
        "greeting": f"Hello, {visitName}!, the temperature is {temperature} degrees Celsius in {client_city}"
    }

    return Response(data)
