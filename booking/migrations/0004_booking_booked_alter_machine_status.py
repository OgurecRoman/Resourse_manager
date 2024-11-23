# Generated by Django 5.1.3 on 2024-11-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0003_alter_booking_id_alter_machine_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="booked",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="machine",
            name="status",
            field=models.CharField(
                choices=[
                    ("ACTIVE", "Active"),
                    ("BOOKED", "Booked"),
                    ("REINSTALLING", "Reinstalling"),
                ],
                default="ACTIVE",
                max_length=50,
            ),
        ),
    ]
