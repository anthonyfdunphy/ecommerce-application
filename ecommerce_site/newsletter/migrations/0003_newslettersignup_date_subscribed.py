# Generated by Django 3.2.17 on 2023-02-18 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_remove_newslettersignup_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersignup',
            name='date_subscribed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]