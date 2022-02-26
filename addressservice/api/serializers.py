from cities_light.models import City
from rest_framework import serializers, validators

from api.models import Address


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ["display_name"]


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "line_one",
            "line_two",
            "line_three",
            "line_four",
            "postcode",
            "city",
        ]
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Address.objects.all(),
                fields=['line_one', 'line_two', 'line_three', 'line_four',
                        'postcode', 'city'],
            )
        ]
