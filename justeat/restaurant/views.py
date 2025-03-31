from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .serializers import RestaurantSerializer
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'restaurant/index.html')

# API endpoint for getting restaurant data from Just Eat API.
class PostcodeView(APIView):
    def get(self, request, postcode):
        try:
            cleaned_postcode = postcode.replace(' ', '').upper() #remove whitespace postcode.
            api_url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{cleaned_postcode}"
            headers = {
                'User-Agent': 'restaurant',
            }           
            response = requests.get(api_url, headers=headers, timeout=5)
            data = response.json().get('restaurants', [])[:10] #get first 10 results.
            serializer = RestaurantSerializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)

            return render(request, 'restaurant/list.html', {
                'postcode' : cleaned_postcode,
                'restaurants' : serializer.validated_data,
            })
        except requests.exceptions.RequestException as err:
            logger.error(f"API request has failed: {str(err)}")
            error_message = "Could not get restaurant data. Please try again later."
            return Response({'ERROR': error_message}, status=500)
            