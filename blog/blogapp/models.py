from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_model(models.Model):
    models.OneToOneField(User,on_delete=models.CASCADE)

    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    secret_name = models.CharField(max_length=200)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.secret_name
    
class post_model(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/',blank=True)
    date = models.DateTimeField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.title