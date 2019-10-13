from django.db import models


class AlcoholModelMixin(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)


class BeerModel(AlcoholModelMixin, models.Model):

    class Meta:
        verbose_name_plural = "Beers"

    def __str__(self):
        return self.name

    BEER_TYPE_CHOICES = [
        ('AL', 'Ale'),
        ('LA', 'Lager'),
        ('ST', 'Stout'),
    ]

    beer_type = models.CharField(
        max_length=2,
        choices=BEER_TYPE_CHOICES,
        default='LA')


class WhiskeyModel(AlcoholModelMixin, models.Model):

    WHISKEY_CHOICES = (
        ('BR', 'Bourbon'),
        ('CN', 'Corn'),
        ('GR', 'Grain')
    )

    whiskey_type = models.CharField(
        max_length=2,
        choices=WHISKEY_CHOICES,
        default='BR'
    )

    def __str__(self):
        return self.name
