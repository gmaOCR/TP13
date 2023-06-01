from django.db import migrations


def check_old_table(apps, schema_editor):
    table_names = schema_editor.connection.introspection.table_names()
    if 'oc_lettings_site_profile' not in table_names:
        raise ValueError("The old profile table 'oc_lettings_site_profile' does not exist.")


def transfer_data(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    User = apps.get_model('auth', 'User')

    old_profiles = OldProfile.objects.all()

    for old_profile in old_profiles:
        new_profile = NewProfile()
        new_profile.user = User.objects.get(id=old_profile.user_id)
        new_profile.favorite_city = old_profile.favorite_city
        new_profile.save()


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(check_old_table, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(transfer_data),
    ]
