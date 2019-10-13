from django.contrib import admin

from . import models


class BeerAdmin(admin.ModelAdmin):

    fields = [
        'name',
        'beer_type',
        'description',
    ]


class WhiskeyAdmin(admin.ModelAdmin):

    fields = [
        'name',
        'whiskey_type',
        'description'
    ]


admin.site.register(models.BeerModel, BeerAdmin)
admin.site.register(models.WhiskeyModel, WhiskeyAdmin)
