# Generated by Django 2.2 on 2019-05-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekty_gminne', '0003_auto_20190501_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projekt',
            old_name='rl_from',
            new_name='okres_realizacji_do',
        ),
        migrations.RenameField(
            model_name='projekt',
            old_name='rl_to',
            new_name='okres_realizacji_od',
        ),
        migrations.AddField(
            model_name='projekt',
            name='instytucja_wdrazajaca',
            field=models.CharField(default='default', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projekt',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]