from django.db import models
from django.urls import reverse

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=128) #max length = required
    text = models.TextField(blank=True, null=True)
    favorited = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("notes:notes-detail", kwargs={"id": self.id})