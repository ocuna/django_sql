from django.db import models
from django.core import validators
from django.urls import reverse

class Students(models.Model):
    first=models.CharField(max_length=30, default='', validators=[validators.MinLengthValidator(2, 'must be 2 characters or more.')])
    last=models.CharField(max_length=30, default='', validators=[validators.MinLengthValidator(2, 'must be 2 characters or more.')])
    email=models.CharField(max_length=254, default='')
    grade=models.FloatField(default=0)

    def get_absolute_url(self):
        #reverse is a custom in-built method that will send the user back to something if this model is utilized to make a record in a form
        # here the user will go back to the url "named" studentdetail and carry with it the argument of the current created private key or ID
        # that way after creation the user can see their own created stuff.
        return reverse('studentDetails', kwargs={'pk':self.pk})