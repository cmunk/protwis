# Generated by Django 2.0.8 on 2019-06-18 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angles', '0006_auto_20190410_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='residueangle',
            name='core_distance',
            field=models.FloatField(default=0, null=True),
        ),
    ]
