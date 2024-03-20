# Generated by Django 5.0.3 on 2024-03-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PageLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('youtube', 'YouTube'), ('tiktok', 'TikTok'), ('x', 'X'), ('facebook', 'Facebook'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'), ('spotify', 'Spotify'), ('apple_music', 'Apple Music'), ('discord', 'Discord'), ('telegram', 'Telegram'), ('whatsapp', 'WhatsApp'), ('tumblr', 'Tumblr'), ('reddit', 'Reddit'), ('cash_app', 'Cash App'), ('paypal', 'PayPal'), ('github', 'GitHub'), ('other', 'Website')], default='other', max_length=255)),
                ('url', models.URLField()),
            ],
        ),
    ]