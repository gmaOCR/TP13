# Generated by Django 3.0 on 2023-05-28 09:25

from django.db import migrations


def delete_old_table(apps, schema_editor):
    table_names = schema_editor.connection.introspection.table_names()
    if 'oc_lettings_site_address' in table_names:
        schema_editor.execute("DROP TABLE oc_lettings_site_address")
    if 'oc_lettings_site_letting' in table_names:
        schema_editor.execute("DROP TABLE oc_lettings_site_letting")


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_auto_20230528_1045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Address'},
        ),
        migrations.RunPython(delete_old_table),
    ]
