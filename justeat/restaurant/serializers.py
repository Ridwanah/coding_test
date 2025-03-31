from rest_framework import serializers

class CuisineSerializer(serializers.Serializer):
    name = serializers.CharField()

class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField()
    cuisines = CuisineSerializer(many=True)
    rating = serializers.DictField()
    address = serializers.DictField()
