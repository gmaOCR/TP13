# Generated by Django 3.0 on 2023-06-01 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_auto_20230601_1138'),
        ('profiles', '0003_auto_20230601_1107'),
        ('lettings', '0003_auto_20230528_1125'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile'
        ),
        migrations.DeleteModel(
            name='Address'
        ),
        migrations.DeleteModel(
            name='Letting'
    ),
    ]

    state_operations = []