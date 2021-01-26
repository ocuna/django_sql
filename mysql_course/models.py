from django.db import models
from django.core import validators

class Courses(models.Model):
    name = models.CharField(max_length=100, default='', validators=[validators.MinLengthValidator(5, 'Must be 5 characters or more.')])
    description = models.TextField(default='')
    instructor = models.CharField(max_length=100, default='', validators=[validators.MinLengthValidator(5, 'Must be 5 characters or more.')])
    # the 'star' value
    rating = models.FloatField(default=0, validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)])

    def __str__(self):
        return str(self.id) + " | " + str(self.name) + " | " + str(self.instructor) + " ---> " + str(self.description)[:30] + "..."