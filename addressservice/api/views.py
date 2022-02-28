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
    serializer_class = AddressSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'line_one',
        'line_two',
        'line_three',
        'line_four',
        'postcode',
    ]

    def get_queryset(self):
        # Retains some API functionality for unauthenticated users
        # Good for a demo and local development, not for production
        if not self.request.user.is_authenticated:
            return Address.objects.filter(user=None)

        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user

        if not self.request.user.is_authenticated:
            user = None

        serializer.is_valid(raise_exception=True)

        # Necessary to add user context in to the serializer
        return serializer.save(user=user)
