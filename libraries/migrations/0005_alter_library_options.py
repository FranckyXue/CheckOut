# Generated by Django 4.2.6 on 2023-11-01 20:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("libraries", "0004_alter_library_table"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="library",
            options={"ordering": ["branch"]},
        ),
    ]
