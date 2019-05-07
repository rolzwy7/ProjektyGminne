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


class KonkursSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Konkurs
        fields = ('id', 'name')


class ProjektSerializer(serializers.ModelSerializer):
    konkurs_id = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Projekt
        fields = (
            'konkurs_id', 'date_added', 'date_modified', 'name', 'instytucja_wdrazajaca',
            'wnioskodawca', 'okres_realizacji_od', 'okres_realizacji_do',
            'wartosc_projektu', 'kwota_dofinansowania', 'waluta',
            'nr_wniosku', 'nr_umowy', 'data_zawarcia_umowy', 'attachment'
        )


class AktywneKonkursySerializer(serializers.ModelSerializer):
    dzielnica_id = DzielnicaSerializer(many=False)

    class Meta:
        model = models.Konkurs
        fields = ('description', 'id', 'date_added', 'date_modified', 'dogrywka',
                  'date_start', 'date_finish', 'name', 'dzielnica_id')


class ZakonczoneKonkursySerializer(serializers.ModelSerializer):
    dzielnica_id = DzielnicaSerializer(many=False)

    class Meta:
        model = models.Konkurs
        fields = ('description', 'id', 'date_added', 'date_modified', 'dogrywka',
                  'date_start', 'date_finish', 'name', 'dzielnica_id')
