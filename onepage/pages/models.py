from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import AppUser


class Page(models.Model):
    """Represents a user's profile page."""

    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    description = models.TextField()


class PageLink(models.Model):
    """Represents a link to a website on a page."""

    class Platform(models.TextChoices):
        """Represents online platforms that can be used to classify website
        links on user pages."""

        YOUTUBE = "youtube", _("YouTube")
        TIKTOK = "tiktok", _("TikTok")
        X = "x", _("X")
        FACEBOOK = "facebook", _("Facebook")
        INSTAGRAM = "instagram", _("Instagram")
        LINKEDIN = "linkedin", _("LinkedIn")
        SPOTIFY = "spotify", _("Spotify")
        APPLE_MUSIC = "apple_music", _("Apple Music")
        DISCORD = "discord", _("Discord")
        TELEGRAM = "telegram", _("Telegram")
        WHATSAPP = "whatsapp", _("WhatsApp")
        TUMBLR = "tumblr", _("Tumblr")
        REDDIT = "reddit", _("Reddit")
        CASH_APP = "cash_app", _("Cash App")
        PAYPAL = "paypal", _("PayPal")
        GITHUB = "github", _("GitHub")
        OTHER = "other", _("Website")

    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    platform = models.CharField(
        max_length=255,
        choices=Platform,
        default=Platform.OTHER,
    )
    url = models.URLField()
