from django.db import models
from django.core import validators

# Create your models here.

class Employee(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    salary=models.FloatField()
    email=models.CharField(max_length=254)
    #anotehr way to display this a certain way in admin...
    #def __str__(self):
    #    return self.email

class Project(models.Model):
    projectName = models.CharField(max_length=50)
    #many to many reference field
    programmers=models.ManyToManyField(Employee)

class Passenger(models.Model):
    first=models.CharField(max_length=30, default='', validators=[validators.MinLengthValidator(2, 'must be 2 characters or more.')])
    last=models.CharField(max_length=30, default='', validators=[validators.MinLengthValidator(2, 'must be 2 characters or more.')])
    email=models.CharField(max_length=254, default='')
    password = models.CharField(max_length=30, default='', validators=[validators.RegexValidator('^(?=.{8,}$)(?=.*[A-Z]).*$', 'Password must be at least 8 characters with 1 being a Capital Letter.')])
    gender = models.CharField(max_length=30, default='')
    ssn = models.IntegerField(default=0)
    points=models.FloatField(default=0)

    def __str__(self):
        return str(self.id) + " | " + str(self.first) + " " + str(self.last) + " ---> " + str(self.points)

class ContactPhone(models.Model):
    type=models.CharField(max_length=10)
    number=models.CharField(max_length=10)
    # on deletions of an employee - the contactPhone should also be deleted.
    # ManytoOne relationship via ForeignKey
    owner=models.ForeignKey(Employee,on_delete=models.CASCADE, null=False)

class Identification(models.Model):
    type=models.CharField(max_length=10)
    number=models.CharField(max_length=10)
    # on deletions of an employee - the contactPhone should also be deleted.
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE)
