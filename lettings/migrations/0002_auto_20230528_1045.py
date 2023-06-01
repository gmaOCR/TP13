from django.db import migrations


def transfer_address_data(apps, schema_editor):
    OcLettingsSiteAddress = apps.get_model('oc_lettings_site', 'Address')
    LettingsAddress = apps.get_model('lettings', 'Address')

    for oc_address in OcLettingsSiteAddress.objects.all():
        lettings_address = LettingsAddress(
            id=oc_address.id,
            street=oc_address.street,
            city=oc_address.city,
            state=oc_address.state,
            zip_code=oc_address.zip_code,
            country_iso_code=oc_address.country_iso_code
        )
        lettings_address.save()


def transfer_letting_data(apps, schema_editor):
    OcLettingsSiteLetting = apps.get_model('oc_lettings_site', 'Letting')
    LettingsLetting = apps.get_model('lettings', 'Letting')

    for oc_letting in OcLettingsSiteLetting.objects.all():
        lettings_letting = LettingsLetting(
            id=oc_letting.id,
            title=oc_letting.title,
            description=oc_letting.description,
            address_id=oc_letting.address_id
        )
        lettings_letting.save()


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(transfer_address_data),
        migrations.RunPython(transfer_letting_data),
    ]
