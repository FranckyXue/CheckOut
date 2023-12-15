# Generated by Django 4.2.6 on 2023-10-21 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('BRANCH', models.CharField(max_length=255)),
                ('ADDRESS', models.CharField(max_length=500)),
                ('CITY', models.CharField(max_length=255)),
                ('POSTCODE', models.CharField(max_length=10)),
                ('PHONE', models.CharField(max_length=20)),
                ('MONDAY', models.CharField(blank=True, max_length=100, null=True)),
                ('TUESDAY', models.CharField(blank=True, max_length=100, null=True)),
                ('WEDNESDAY', models.CharField(blank=True, max_length=100, null=True)),
                ('THURSDAY', models.CharField(blank=True, max_length=100, null=True)),
                ('FRIDAY', models.CharField(blank=True, max_length=100, null=True)),
                ('SATURDAY', models.CharField(blank=True, max_length=100, null=True)),
                ('SUNDAY', models.CharField(blank=True, max_length=100, null=True)),
                ('LATITUDE', models.DecimalField(decimal_places=6, max_digits=10)),
                ('LONGITUDE', models.DecimalField(decimal_places=6, max_digits=10)),
                ('LINK', models.URLField(blank=True, max_length=1000, null=True)),
                ('NYU', models.CharField(max_length=255)),
            ],
        ),
    ]
