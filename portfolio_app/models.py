from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    profession= models.CharField(max_length=50)
    bio= models.TextField(max_length=1000)
    github_url= models.URLField(max_length=200)
    instagram_url= models.URLField(max_length=200)
    linkedin_url=models.URLField(max_length=200)
    profile_picture=models.ImageField(upload_to="images/",null=True,blank=True)

    def __str__(self):
        return self.name

