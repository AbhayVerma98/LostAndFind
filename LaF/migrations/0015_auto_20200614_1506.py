# Generated by Django 3.0.6 on 2020-06-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaF', '0014_auto_20200613_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='find',
            name='age',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
