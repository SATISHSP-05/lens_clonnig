from django.db import migrations


def seed_delivery_pincodes(apps, schema_editor):
    DeliveryPincode = apps.get_model("store", "DeliveryPincode")
    DeliveryPincode.objects.update_or_create(
        pincode="572201",
        defaults={
            "city": "",
            "state": "",
            "delivery_days": 3,
            "active": True,
            "source": "seed",
        },
    )


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0008_deliverypincode"),
    ]

    operations = [
        migrations.RunPython(seed_delivery_pincodes, migrations.RunPython.noop),
    ]
