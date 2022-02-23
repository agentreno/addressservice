from address.models import Address
from rest_framework import serializers


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "raw",
            "street_number",
            "route",
            "locality",
        ]
