# Generated by Django 4.0.4 on 2022-05-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chemin', models.ImageField(blank=True, null=True, upload_to='static/filepath')),
            ],
        ),
    ]
