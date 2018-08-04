from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    date_created = models.DateField()

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)
    creator = models.CharField(max_length=20)
    paradigm = models.CharField(max_length=20)
    date_created = models.DateField()

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    #COMPANY - one to many - one company can have multiple programmers -- programmer has ONE company
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    #LANGUAGES ManyToManyField --  many to many -- 
    #many programmers can know many languages AND languages can know many programmers
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
