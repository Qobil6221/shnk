from django.db import models
from django.contrib.auth import get_user_model


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True
        db_table = 'abstract_model'


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

class Boglanish(models.Model):
    FIO = models.CharField(max_length = 128)
    email = models.CharField(max_length = 128)
    telefon = models.CharField(max_length = 128)
    rahbariyat = models.ForeignKey(Rahbariyat, on_delete=models.PROTECT, related_name='contacts',)
    text = models.TextField()
    img = models.ImageField(default="media\default.jpg")
    manzili = models.CharField(max_length = 128)

class Qurilish_reglamentlari(models.Model):
    number = models.IntegerField()
    belgilanishi = models.CharField(max_length = 55)
    nomi = models.CharField(max_length = 255)
    hujjat = models.FileField()

class ESF(models.Model):
    hujjat_raqami = models.IntegerField()
    kalit_soz = models.CharField(max_length = 255)
    
class Lugat(models.Model):
    num = models.IntegerField()
    rus = models.TextField(max_length = 20)
    uzb = models.TextField(max_length = 20)
    turk = models.TextField(max_length = 20)
    eng = models.TextField(max_length = 20)

class SHNKSystemsModel(AbstractBaseModel):
    code = models.CharField(max_length=2, unique=True)
    system_name_uz = models.CharField(max_length=255, unique=True)
    system_name_ru = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.system_name_uz}"

    class Meta:
        db_table = 'shnk_systems'
        verbose_name_plural = 'SHNK systems'


class SHNKGroupsModel(AbstractBaseModel):
    group_code = models.CharField(max_length=15)
    group_name_uz = models.CharField(max_length=255)
    group_name_ru = models.CharField(max_length=255)
    group_system = models.ForeignKey(SHNKSystemsModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group_code} - {self.group_name_uz}"

    class Meta:
        db_table = 'shnk_groups'
        verbose_name_plural = 'SHNK groups'


class SHNKTypesModel(AbstractBaseModel):
    type_name_uz = models.CharField(max_length=10, unique=True)
    type_name_ru = models.CharField(max_length=10, unique=True, null=True)
    type_description_uz = models.CharField(max_length=255, null=True)
    type_description_ru = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.type_name_uz} - {self.type_description_uz}"

    class Meta:
        db_table = 'shnk_types'
        verbose_name_plural = 'SHNK types'


class SHNKDocumentsModel(AbstractBaseModel):
    shnk_name_uz = models.CharField(max_length=255, unique=True)
    shnk_name_ru = models.CharField(max_length=255, unique=True, null=True)
    shnk_code = models.CharField(max_length=10)
    shnk_type = models.ForeignKey(SHNKTypesModel, on_delete=models.CASCADE)
    shnk_file_uz = models.FileField(upload_to='shnk', null=True, blank=True)
    shnk_file_ru = models.FileField(upload_to='shnk', null=True, blank=True)
    shnk_group = models.ForeignKey(SHNKGroupsModel, on_delete=models.CASCADE)
    shnk_rating = models.JSONField(default=list)

    def __str__(self):
        return f"{self.shnk_name_uz} - {self.shnk_name_ru}"

    class Meta:
        db_table = 'shnk_documents'
        verbose_name_plural = 'SHNK documents'