# Generated by Django 4.1.7 on 2023-06-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_alter_challenge_challenge_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='challenge_file',
        ),
        migrations.AddField(
            model_name='challenge',
            name='challenge_file_link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
