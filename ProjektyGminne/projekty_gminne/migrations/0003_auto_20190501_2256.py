# Generated by Django 2.2 on 2019-05-01 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekty_gminne', '0002_auto_20190501_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dzielnica',
            old_name='projekt_id',
            new_name='gmina_id',
        ),
    ]
