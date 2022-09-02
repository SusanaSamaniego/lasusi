from django.db import models

# Create your models here.
class student(models.Model):
 nuevo = models.IntegerField(primary_key=True)
first_name = models.CharField(max_length=30)
last_name = models.CharField(max_length=30)
telefono = models.BinaryField
email = models.EmailField(mailbox)
list =models.TextField(max_length=30)
edit=models.TextField(max_length=30)
delete =models.TextField(Delete )
def __str__(self):
  return '{} {}' .format(self.first_name,self.last_name,self.e-mail)

class matricula (models.Model):
 level =models.TextField
name= models.CharField(max_length=30)
alumno= models.CharField(max_length=30)
profesor= models.TextField(max_length=28)
def __str__(self):
    return '{} {}'. format (self.alumno, self.profesor, self.level)


class pago (models.Model):
 date_of_page = models.DateTimeField
cuantity =models.Count
def __str__(self):
    return self.date
    return self.cuantity
def get_absolute_url(self):datetime

 
class User (models.Model):
 first_name =models.TextField(max_length=25)
last_name=models.TextField(max_length=20)
telefono= models.IntegerField(max_length=15)
edad= models.IntegerField(max_length=2)
email=models.EmailField(max_length=30)
ciudad= models.IntegerField(max_length=18)
