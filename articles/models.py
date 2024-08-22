from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to="uploads")
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("updated", "published")

    def __str__(self):
        return self.title
