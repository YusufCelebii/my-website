from django.db import models
import logging
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50,verbose_name="İsim-Soyisim")
    profession= models.CharField(max_length=50,verbose_name="Meslek")
    bio= models.TextField(max_length=1000,verbose_name="Hakkında")

    social_links= models.JSONField(default=dict,blank=True,verbose_name="Sosyal Medya bağlantıları")
    communication_links= models.JSONField(default=dict,blank=True,verbose_name="İletişim Bilgileri")
    profile_picture=models.ImageField(
        upload_to="images/",
        null=True,
        blank=True,
        verbose_name="Profil Resmi"
    )

    class Meta():
        verbose_name="Profile Card Section"


    def save(self, *args, **kwargs):
        
        if not self.pk and Profile.objects.exists():
            print("Alresady Exists")
            return  # Hata mesajı göster ve işlemi durdur  
        
        super(Profile,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

