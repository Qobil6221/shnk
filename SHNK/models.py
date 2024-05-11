from django.db import models

class Xabarlar(models.Model):
    title = models.CharField(max_length = 255, blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    img = models.ImageField(default="media\default.jpg")
    date = models.CharField(max_length = 10, blank = True, null = True)

class Elonlar(models.Model):
    title = models.CharField(max_length = 255, blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    date = models.CharField(max_length = 10, blank = True, null = True)

class Rahbariyat(models.Model):
    name = models.CharField(max_length = 75)
    lavozimi = models.CharField(max_length = 255)
    qabul_kunlari = models.CharField(max_length = 255)
    telefon = models.CharField(max_length = 75)
    email = models.EmailField()
    img = models.ImageField(default="media\default.jpg")

class Tarkibiy_bolinmalar(models.Model):
    name = models.CharField(max_length = 75)
    lavozimi = models.CharField(max_length = 255)
    qabul_kunlari = models.CharField(max_length = 255)
    telefon = models.CharField(max_length = 75)
    email = models.EmailField()
    img = models.ImageField(default="media\default.jpg") 

class Standartlar(models.Model):
    title = models.CharField(max_length = 255, blank = True, null = True)
    description = models.TextField(blank = True, null = True)