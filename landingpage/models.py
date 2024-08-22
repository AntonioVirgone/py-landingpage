from django.db import models

# Create your models here.
class Landingpage(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    