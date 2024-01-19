from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=60)
    subtitle= models.CharField(max_length=90)
    description = models.TextField(max_length=250)
    author= models.ForeignKey(User, on_delete=models.CASCADE),
    create_at=models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"{self.author}"
    
   
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f"{self.user}"
