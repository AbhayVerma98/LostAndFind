# Generated by Django 3.0.6 on 2020-06-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaF', '0010_auto_20200603_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
