# Generated by Django 5.1.4 on 2025-01-19 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated_at']},
        ),
    ]
