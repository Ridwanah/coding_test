from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

def index(request):
    return render(request, 'restaurant/index.html')

class PostcodeView(APIView):
    def get(self, request, postcode):
        cleaned_postcode = postcode.replace(' ', '').upper()
        api_url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{cleaned_postcode}"
        headers = {
            'User-Agent': 'restaurant' 
        }           
        response = requests.get(api_url, headers=headers, timeout=5)
        data = response.json().get('restaurants', [])[:10]
        restaurant_data = []
        for restaurant in data:
            values = {
                'name' : restaurant.get('name'),
                'cuisines' : restaurant.get('cuisines'),
                'rating' : (restaurant.get('rating')).get('starRating'),
                'address' : restaurant.get('address'),
            }
            restaurant_data.append(values)
        return Response(restaurant_data)
            