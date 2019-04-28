from django.db import models


class Konkurs(models.Model):
    class Meta:
        verbose_name_plural = "Konkursy"
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    date_finish = models.DateTimeField(null=False)
    name = models.CharField(max_length=256, null=False)


class Gmina(models.Model):
    class Meta:
        verbose_name_plural = "Gminy"
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=128, null=False)


class Dzielnica(models.Model):
    class Meta:
        verbose_name_plural = "Dzielnice"
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    projekt_id = models.ForeignKey(
        'Gmina', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False)


class Projekt(models.Model):
    class Meta:
        verbose_name_plural = "Projekty"
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    konkurs_id = models.ForeignKey(
        'Konkurs', null=False, on_delete=models.CASCADE)
    dzielnica_id = models.ForeignKey(
        'Dzielnica', null=False, on_delete=models.CASCADE)

    name = models.CharField(max_length=256, null=False)

    rl_from = models.DateTimeField(null=False)
    rl_to = models.DateTimeField(null=False)

    name = models.CharField(max_length=22, null=False)

    project_value = models.DecimalField(max_digits=6, decimal_places=2)
    project_funds = models.DecimalField(max_digits=6, decimal_places=2)

    attachment = models.FileField(upload_to='attachments/projects')


class Glos(models.Model):
    class Meta:
        verbose_name_plural = "Głosy"
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=11, null=False)

    projekt_id = models.ForeignKey(
        'Projekt', null=False, on_delete=models.CASCADE)
