# Generated by Django 4.1.7 on 2023-05-22 12:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("challenges", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="challenge_file",
            field=models.FileField(blank=True, upload_to="challenges/"),
        ),
        migrations.AlterField(
            model_name="challenge",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
