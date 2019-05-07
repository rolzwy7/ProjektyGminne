from django.db import models

CURRENCY = (
    ('PLN', 'PLN'),
    ('USD', 'USD'),
    ('EUR', 'EUR')
)


class Gmina(models.Model):
    class Meta:
        verbose_name_plural = "Gminy"
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name


class Dzielnica(models.Model):
    class Meta:
        verbose_name_plural = "Dzielnice"
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    gmina_id = models.ForeignKey(
        'Gmina', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name


class Konkurs(models.Model):
    class Meta:
        verbose_name_plural = "Konkursy"
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    dogrywka = models.BooleanField(default=False)

    dzielnica_id = models.ForeignKey(
        'Dzielnica', null=False, on_delete=models.CASCADE)

    date_start = models.DateTimeField(null=False)
    date_finish = models.DateTimeField(null=False)

    name = models.CharField(max_length=256, null=False)
    description = models.TextField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return self.name


class Projekt(models.Model):
    class Meta:
        verbose_name_plural = "Projekty"
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    konkurs_id = models.ForeignKey(
        'Konkurs', on_delete=models.CASCADE)

    name = models.CharField(max_length=256, null=False)

    instytucja_wdrazajaca = models.CharField(max_length=256, null=False)
    wnioskodawca = models.CharField(max_length=128, null=False)

    # okres realizacji
    okres_realizacji_od = models.DateField(null=False)
    okres_realizacji_do = models.DateField(null=False)

    wartosc_projektu = models.CharField(max_length=32)
    kwota_dofinansowania = models.CharField(max_length=32)
    waluta = models.CharField(choices=CURRENCY, max_length=3, default="PLN")

    # po zawarciu umowy
    nr_wniosku = models.CharField(blank=True, null=True, max_length=32)
    nr_umowy = models.CharField(blank=True, null=True, max_length=32)
    data_zawarcia_umowy = models.DateField(blank=True, null=True)

    attachment = models.FileField(blank=True, null=True, upload_to='attachments/projects')

    description = models.TextField(max_length=1024, null=False)

    def __str__(self):
        return self.name


class Glos(models.Model):
    class Meta:
        verbose_name_plural = "Głosy"
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=11, null=False)

    projekt_id = models.ForeignKey(
        'Projekt', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Symulacja API
class ApiMockData(models.Model):
    class Meta:
        verbose_name_plural = "ApiMockData"
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    dzielnica_id = models.ForeignKey(
        'Dzielnica', null=False, on_delete=models.CASCADE)
    pesel = models.CharField(max_length=11, null=False)

    def __str__(self):
        return self.pesel
