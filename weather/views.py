from django.shortcuts import render
from .weather_service import get_weather

def weather_view(request):
    city = request.GET.get('city')
    weather_data = None

    if city:
        weather_data = get_weather(city)

    context = {
        'weather_data': weather_data
    }
    return render(request, 'weather.html', context)
