# Generated by Django 4.1.7 on 2023-06-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='challenge_file',
            field=models.FileField(blank=True, upload_to='media/challenges/'),
        ),
    ]