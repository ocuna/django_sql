from django.db import models

# Create your models here.

class Employee(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    salary=models.FloatField()
    email=models.CharField(max_length=254)

    #anotehr way to display this a certain way in admin...
    #def __str__(self):
    #    return self.email


class Passenger(models.Model):
    first=models.CharField(max_length=30, default='')
    last=models.CharField(max_length=30, default='')
    email=models.CharField(max_length=254, default='')
    password = models.CharField(max_length=30, default='')
    gender = models.CharField(max_length=30, default='')
    ssn = models.IntegerField(default=0)
    points=models.FloatField(default=0)

    def __str__(self):
        return str(self.id) + " | " + str(self.first) + " " + str(self.last) + " ---> " + str(self.points)