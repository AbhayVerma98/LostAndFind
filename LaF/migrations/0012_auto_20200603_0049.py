# Generated by Django 3.0.6 on 2020-06-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaF', '0011_auto_20200603_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
