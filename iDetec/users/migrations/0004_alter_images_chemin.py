# Generated by Django 4.0.4 on 2022-05-15 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_anomaly_pixel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='chemin',
            field=models.ImageField(blank=True, null=True, upload_to='imageAno'),
        ),
    ]