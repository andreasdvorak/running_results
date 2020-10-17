from django.db import models
from django.urls import reverse
# Create your models here.

class Role(models.Model):
    role = models.CharField(max_length=10)
    
    def __str__(self):
        return self.role

class User(models.Model):
    firstname   = models.CharField(max_length=40)
    lastname    = models.CharField(max_length=40)
    username    = models.CharField(max_length=40)
    email       = models.CharField(max_length=40)
    password    = models.CharField(max_length=40)
    role        = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
 
    # do not show 'xxx Object' but username in admin 
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("user:user-detail", kwargs={"id": self.id}) #f"/user/{self.id}/" # app_name::name in urls.py