# Generated by Django 4.0.1 on 2022-03-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='age',
            field=models.IntegerField(default=25),
        ),
        migrations.AddField(
            model_name='lead',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
