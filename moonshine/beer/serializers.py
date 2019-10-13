from rest_framework import fields, serializers
from beer import models


class BeerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BeerModel

        fields = (
            'name',
            'beer_type',
            'description',
        )


class WhiskeyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WhiskeyModel
        fields = '__all__'