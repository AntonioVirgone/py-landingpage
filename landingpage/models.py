from django.db import models

# Create your models here.
class Landingpage(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    cards = [0,1]
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    