from django.db import models

# Create your models here.
class Membership(models.Model):
    person = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    invite_reason = models.CharField(max_length=64)
    images = models.ImageField(upload_to = "images" ,default="")
    def __str__(self):
        return self.person

