from cities_light.models import Country, City
from django.test import TestCase
from rest_framework.test import APIClient

from api.models import Address


class AddressTests(TestCase):
    def test_address_list_success(self):
        client = APIClient()
        address = Address(
            line_one='testline',
            postcode='testpostcode',
        )
        address.save()

        response_data = client.get('/address/', format='json').json()
        self.assertEqual(response_data['count'], 1)
        self.assertEqual(response_data['results'][0]['line_one'], 'testline')
        self.assertEqual(response_data['results'][0]['postcode'], 'testpostcode')

    def test_address_get_success(self):
        client = APIClient()
        address = Address(
            line_one='testline',
            postcode='testpostcode',
        )
        address.save()

        response_data = client.get('/address/1/', format='json').json()
        self.assertEqual(response_data['line_one'], 'testline')
        self.assertEqual(response_data['postcode'], 'testpostcode')

    def test_address_delete_success(self):
        client = APIClient()
        address = Address(
            line_one='testline',
            postcode='testpostcode',
        )
        address.save()

        response = client.delete('/address/1/', format='json')
        self.assertEqual(response.status_code, 204)

    def test_address_create_success(self):
        client = APIClient()

        response = client.post('/address/', {
            'line_one': 'testline',
            'line_two': '',
            'line_three': '',
            'line_four': '',
            'city': None,
            'postcode': 'testpostcode',
        }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_address_update_success(self):
        client = APIClient()
        address = Address(
            line_one='testline',
            postcode='testpostcode',
        )
        address.save()

        response = client.put('/address/1/', {
            'line_one': 'changed',
            'line_two': '',
            'line_three': '',
            'line_four': '',
            'city': None,
            'postcode': 'testpostcode',
        }, format='json')

        address.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(address.line_one, 'changed')

    def test_address_create_duplicate_fails(self):
        client = APIClient()
        country = Country.objects.create(tld='GB', continent='EU', name_ascii='GB')
        City.objects.create(display_name='testcity', name_ascii='testcity', country=country)

        response = client.post('/address/', {
            'line_one': 'testline',
            'line_two': '',
            'line_three': '',
            'line_four': '',
            'city': 'http://testserver/city/1/',
            'postcode': 'testpostcode',
        }, format='json')

        second_response = client.post('/address/', {
            'line_one': 'testline',
            'line_two': '',
            'line_three': '',
            'line_four': '',
            'city': 'http://testserver/city/1/',
            'postcode': 'testpostcode',
        }, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(second_response.status_code, 400)
