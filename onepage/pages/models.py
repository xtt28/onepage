from urllib.parse import quote_plus

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import AppUser


class Page(models.Model):
    """Represents a user's profile page."""

    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s page"


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
        SPOTIFY = "spotify", _("Spotify Artist ID")
        DISCORD = "discord", _("Discord Invite ID")
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
        choices=Platform.choices,
        default=Platform.OTHER,
    )
    value = models.TextField()

    def get_profile_link(self):
        safe_value = quote_plus(self.value)
        match self.platform:
            case "youtube" | "tiktok" | "x" | "tumblr":
                return f"https://{self.platform}.com/@{safe_value}"
            case "facebook" | "instagram" | "github":
                return f"https://{self.platform}.com/{safe_value}"
            case "spotify":
                return f"https://open.spotify.com/artist/{safe_value}"
            case "discord":
                return f"https://discord.com/invite/{safe_value}"
            case "telegram":
                return f"https://t.me/{safe_value}"
            case "whatsapp":
                return f"https://chat.whatsapp.com/{safe_value}"
            case "reddit":
                return f"https://reddit.com/u/{safe_value}"
            case "cash_app":
                return f"https://cash.app/{safe_value}"
            case "paypal":
                return f"https://paypal.me/{safe_value}"
            case "other" | _:
                validate_url = URLValidator()

                try:
                    validate_url(self.value)
                    return self.value
                except ValidationError:
                    return ""

    def __str__(self):
        return f"{self.platform} link: {self.value}"
