# Generated by Django 5.0.3 on 2024-03-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_alter_pagelink_platform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pagelink",
            name="value",
            field=models.CharField(max_length=1000),
        ),
    ]
