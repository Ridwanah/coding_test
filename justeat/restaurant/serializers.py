from rest_framework import serializers

# Serializes cuisine data from Just Eat API response.
class CuisineSerializer(serializers.Serializer):
    name = serializers.CharField()

# Converts Just Eat API restauarnt data into Python objects
# based on selected fields" 'name', 'cuisines', 'rating', 'address'.
class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField()
    cuisines = CuisineSerializer(many=True)
    rating = serializers.DictField()
    address = serializers.DictField()
