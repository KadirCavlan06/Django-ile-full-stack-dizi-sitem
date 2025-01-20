from django.db import models

# Create your models here.


class kategori_db(models.Model):
    name=models.TextField()

    
    
class diziler_db(models.Model):
    dizi_adi= models.TextField()
    dizi_aciklama= models.TextField()
    dizi_konusu= models.TextField()
    dizi_imbd= models.TextField()
    dizi_gorsel= models.TextField()
    anasayfa= models.BooleanField(default=False)
