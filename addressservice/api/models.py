from cities_light.models import City
from django.db import models


class Address(models.Model):
    line_one = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    line_two = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    line_three = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    line_four = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    postcode = models.CharField(max_length=20)
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['line_one', 'line_two', 'line_three', 'line_four',
                        'postcode', 'city'], name='unique_address'
            )
        ]
