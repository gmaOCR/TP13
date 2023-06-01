from django.contrib.auth.models import User
from django.db import migrations
from oc_lettings_site.models import Profile as OldProfile
from profiles.models import Profile as NewProfile


def check_old_table(apps, schema_editor):
    table_names = schema_editor.connection.introspection.table_names()
    if 'oc_lettings_site_profile' not in table_names:
        raise ValueError("The old profile table 'oc_lettings_site_profile' does not exist.")


def transfer_data(apps, schema_editor):
    old_profiles = OldProfile.objects.all()

    for old_profile in old_profiles:
        new_profile = NewProfile()
        new_profile.user = User.objects.get(id=old_profile.user_id)
        new_profile.favorite_city = old_profile.favorite_city
        new_profile.save()


def delete_old_table(apps, schema_editor):
    schema_editor.connection.execute("DROP TABLE oc_lettings_site_profile")


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(check_old_table, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(transfer_data),
        migrations.RunPython(delete_old_table),
    ]
