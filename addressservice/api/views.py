from cities_light.models import City
from rest_framework import filters, viewsets

from api.models import Address
from api.serializers import AddressSerializer, CitySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['search_names']


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'line_one',
        'line_two',
        'line_three',
        'line_four',
        'postcode',
    ]
