from projekty_gminne.models import ApiMockData, Dzielnica, Gmina
from rest_framework import serializers


class ApiMockDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiMockData
        fields = ('date_added', 'date_modified', 'pesel', 'dzielnica_id')


class GminaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gmina
        fields = ('date_added', 'date_modified', 'name')


class DzielnicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dzielnica
        fields = ('date_added', 'date_modified', 'name', 'gmina_id')
