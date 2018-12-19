from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Champion(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    alias = models.CharField(max_length=100)
    quote = models.CharField(max_length=255)
    biography = models.TextField()

    FIGHTER = 1
    ASSASSIN = 2
    TANK = 3
    MAGE = 4
    MARKSMAN = 5
    SUPPORT = 6
    ROLE_CHOICES = (
        (FIGHTER, 'Fighter'),
        (ASSASSIN, "Assassin"),
        (TANK, "Tank"),
        (MAGE, "Mage"),
        (MARKSMAN, "Marksman"),
        (SUPPORT, "Support"),
    )
    role = models.IntegerField(default=0, choices=ROLE_CHOICES)
    youtube_video_id = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to="champions_avatars/", blank=True)
    wallpaper = models.ImageField(upload_to="champions_wallpapers/", blank=True)


@receiver(pre_save, sender=Champion)
def pre_save_event(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
