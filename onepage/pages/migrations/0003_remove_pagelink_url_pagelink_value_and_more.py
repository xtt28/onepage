# Generated by Django 5.0.3 on 2024-03-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pagelink",
            name="url",
        ),
        migrations.AddField(
            model_name="pagelink",
            name="value",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="page",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="pagelink",
            name="platform",
            field=models.CharField(
                choices=[
                    ("youtube", "YouTube"),
                    ("tiktok", "TikTok"),
                    ("x", "X"),
                    ("facebook", "Facebook"),
                    ("instagram", "Instagram"),
                    ("linkedin", "LinkedIn"),
                    ("spotify", "Spotify Artist ID"),
                    ("discord", "Discord Invite ID"),
                    ("telegram", "Telegram"),
                    ("whatsapp", "WhatsApp"),
                    ("tumblr", "Tumblr"),
                    ("reddit", "Reddit"),
                    ("cash_app", "Cash App"),
                    ("paypal", "PayPal"),
                    ("github", "GitHub"),
                    ("other", "Website"),
                ],
                default="other",
                max_length=255,
            ),
        ),
    ]