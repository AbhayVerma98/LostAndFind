# Generated by Django 3.0.6 on 2020-06-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaF', '0006_lose'),
    ]

    operations = [
        migrations.AddField(
            model_name='man',
            name='city_or_village',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='man',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='man',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
