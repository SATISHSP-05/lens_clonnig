from django.db import migrations


def seed_more_delivery_pincodes(apps, schema_editor):
    DeliveryPincode = apps.get_model("store", "DeliveryPincode")
    pincodes = [
        ("560001", "Bengaluru", "Karnataka"),
        ("560034", "Bengaluru", "Karnataka"),
        ("110001", "New Delhi", "Delhi"),
        ("400001", "Mumbai", "Maharashtra"),
        ("600001", "Chennai", "Tamil Nadu"),
        ("700001", "Kolkata", "West Bengal"),
        ("500001", "Hyderabad", "Telangana"),
        ("302001", "Jaipur", "Rajasthan"),
        ("411001", "Pune", "Maharashtra"),
        ("380001", "Ahmedabad", "Gujarat"),
    ]
    for pin, city, state in pincodes:
        DeliveryPincode.objects.update_or_create(
            pincode=pin,
            defaults={
                "city": city,
                "state": state,
                "delivery_days": 3,
                "active": True,
                "source": "seed",
            },
        )


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0009_seed_deliverypincode"),
    ]

    operations = [
        migrations.RunPython(seed_more_delivery_pincodes, migrations.RunPython.noop),
    ]
