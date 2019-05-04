from projekty_gminne import models
from rest_framework import serializers


class ApiMockDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ApiMockData
        fields = ('date_added', 'date_modified', 'pesel', 'dzielnica_id')


class GminaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Gmina
        fields = ('date_added', 'date_modified', 'name')


class DzielnicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Dzielnica
        fields = ('date_added', 'date_modified', 'name', 'gmina_id')


class GlosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Glos
        fields = ('date_added', 'date_modified')


class AktywneKonkursySerializer(serializers.ModelSerializer):
    dzielnica_id = DzielnicaSerializer(many=False)

    class Meta:
        model = models.Konkurs
        fields = ('date_added', 'date_modified', 'dogrywka', #  'description',
                  'date_start', 'date_finish', 'name', 'dzielnica_id')


class ZakonczoneKonkursySerializer(serializers.ModelSerializer):
    dzielnica_id = DzielnicaSerializer(many=False)

    class Meta:
        model = models.Konkurs
        fields = ('date_added', 'date_modified', 'dogrywka', #  'description',
                  'date_start', 'date_finish', 'name', 'dzielnica_id')
