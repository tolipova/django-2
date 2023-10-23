from django.db import models

# Create your models here.
class Malumot(models.Model):
    ism = models.CharField(max_length=255)
    about = models.TextField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='user_info/')
    
    def __str__(self):
        return self.ism