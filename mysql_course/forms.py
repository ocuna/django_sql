from django.forms import ModelForm, Textarea
from mysql_course.models import Courses
from django.core import validators
import re

# inheriting the "modelForm" class into this custom class helps setup quick forms using models as the basis
class coursesModelForm(ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'
        widgets = {
            'description' : Textarea()
        }