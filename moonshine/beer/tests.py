import json

from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from .models import BeerModel
from .models import WhiskeyModel
from .serializers import BeerModelSerializer
from .serializers import WhiskeyModelSerializer


class GetAlcoholTests(TestCase):
    def setUp(self):
        self.beer = BeerModel.objects.create(
            name='Heineken',
            beer_type='AL',
            description='valid beer'
        )
        self.beer_serializer = BeerModelSerializer(self.beer)

        self.whiskey = WhiskeyModel.objects.create(
            name='Johnnie Walker',
            whiskey_type='BR',
            description='valid whiskey'
        )
        self.whiskey_serializer = WhiskeyModelSerializer(self.whiskey)

    def test_beer_retrieve(self):
        resp = self.client.get(
            reverse(
                'beer:beer-get',
                kwargs={
                    'pk': self.beer.pk
                }
            ),
        )

        self.assertEqual(resp.data, self.beer_serializer.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_whiskey_retrieve(self):
        resp = self.client.get(
            reverse(
                'beer:whiskey-detail',
                kwargs={
                    'pk': self.whiskey.pk
                }
            ),
        )

        self.assertEqual(resp.data, self.whiskey_serializer.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_whiskey_list(self):
        resp = self.client.get(reverse('beer:whiskey-list'))
        self.assertEqual(resp.data[0], self.whiskey_serializer.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)


class PostAlcoholTests(TestCase):

    def setUp(self):
        self.valid_beer= {
                'name': 'Heineken',
                'beer_type': 'AL',
                'description': 'valid beer'
        }
        self.invalid_beer = {
                'name': 'CrapBeer',
                'beer_type': 'bla',
                'description': 'invalid beer'
        }

        self.valid_whiskey = {
                'name': 'Evan Williams',
                'whiskey_type': 'BR',
                'description': 'valid whiskey'
        }
        self.invalid_whiskey = {
            'name': 'CrapWhiskey',
            'whiskey_type': 'crap',
            'description': 'invalid whiskey'
        }

    def test_valid_beer_post(self):
        resp = self.client.post(
            reverse('beer:beer-post'),
            data=json.dumps(self.valid_beer),
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_invalid_beer_post(self):
        resp = self.client.post(
            reverse('beer:beer-post'),
            data=json.dumps(self.invalid_beer),
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_whiskey_post(self):
        resp = self.client.post(
            reverse('beer:whiskey-list'),
            data=json.dumps(self.valid_whiskey),
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_invalid_whiskey_post(self):
        resp = self.client.post(
            reverse('beer:whiskey-list'),
            data=json.dumps(self.invalid_whiskey),
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
