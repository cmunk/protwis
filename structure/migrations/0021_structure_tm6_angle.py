# Generated by Django 2.0.8 on 2019-07-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0020_structure_class_contact_representative'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='tm6_angle',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
