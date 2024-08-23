from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to="uploads", blank=True)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-updated", "-published")

    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("articles:article-detail", args=[self.slug])
    
    
    def isLBigArticle(self):
        return len(self.content) > 280
    
