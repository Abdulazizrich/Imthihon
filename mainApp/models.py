from django.db import models
from django.contrib.auth.models import User
class Bolim(models.Model):
    nom = models.CharField(max_length=30)
    haqida = models.TextField()
    def __str__(self):
        return  f'{self.nom}'

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    tirik = models.BooleanField()
    mamalakat = models.CharField(max_length=30)

    def __str__(self):
        return  f'{self.ism}'


class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    yil = models.DateField()
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tasks')
    file = models.FileField(upload_to='uploads')
    def __str__(self):
        return  f'{self.nom}'
