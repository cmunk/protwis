# Generated by Django 2.0.8 on 2019-08-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angles', '0008_auto_20190717_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='residueangle',
            name='mid_distance',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='residueangle',
            name='midplane_distance',
            field=models.FloatField(default=0, null=True),
        ),
    ]
