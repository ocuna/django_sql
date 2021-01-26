from django.forms import ModelForm, Select, Form, CharField, IntegerField, ValidationError, EmailInput, PasswordInput
from mysql_hr.models import Passenger
from django.core import validators
from django.core.validators import RegexValidator
import re

# inheriting the "modelForm" class into this custom class helps setup quick forms using models as the basis
class modelPassengerRegistration(ModelForm):
    class Meta:
        GENDERS = [('male','MALE'),('female','FEMALE'),('imaginary','Imaginary')]
        model = Passenger
        fields = '__all__'
        widgets = {
            'gender' : Select(choices=GENDERS),
            'email' : EmailInput(attrs={'class': 'd-block'}),
            'password' : PasswordInput(render_value = True, attrs={'class': 'd-block'}),
        }
        validators = {
            'first' : validators.MinLengthValidator(2),
            'last' : validators.MinLengthValidator(2),
            'password' : RegexValidator('^(?=.{8,}$)(?=.*[A-Z]).*$', 'password is not correct')
        }

class passengerRegistration(Form):
    GENDERS = [('male','MALE'),('female','FEMALE'),('imaginary','Imaginary')]
    first = CharField(max_length=30,validators=[validators.MinLengthValidator(2)])
    last = CharField(max_length=30,validators=[validators.MinLengthValidator(2)])
    email = CharField(label='Is your UserName - it will later be used to login after registration',max_length=254,widget=EmailInput(attrs={'class': 'd-block'}))
    password = CharField(label='Must contain 8 characters at least, and 1 captial letter.',max_length=30,widget=PasswordInput(attrs={'class': 'd-block'}))
    ssn = IntegerField(required=False)
    gender = CharField(widget=Select(choices=GENDERS))

    def clean(self):
        #super-class() is available for any class that wants to reference whatever methods were instantiated by inherited classes
        user_clean_data = super().clean()
        inputssn = user_clean_data['ssn']
        # ssn regex match
        if not re.match(r'^(?!000|.+0{4})(?:\d{9}|\d{3}-\d{2}-\d{4})$', str(inputssn)) :
            raise ValidationError(str(inputssn) + ': is not a valid SSN')

        password = user_clean_data['password']
        # password regex match
        if not re.match(r'^(?=.{8,}$)(?=.*[A-Z]).*$', str(password)) :
            raise ValidationError('Password is not valid password')

class passengerLogin(Form):
    email = CharField(label='UserName (email used to register)',max_length=254,widget=EmailInput)
    password = CharField(label='Must contain 8 characters at least, and 1 captial letter.',max_length=30,widget=PasswordInput)

    def clean(self):
        user_clean_data = super().clean()
        password = user_clean_data['password']
        # password regex match - must be 8 Characters with at least 1 capital letter
        if not re.match(r'^(?=.{8,}$)(?=.*[A-Z]).*$', str(password)) :
            raise ValidationError('The password provided is not a valid password')

# the below function is a one-off verification method based on the pattern clean_yourFormObject
'''
    def clean_ssn(self):
        inputssn = self.cleaned_data['ssn']
        # ssn regex match
        if not re.match(r'^(?!000|.+0{4})(?:\d{9}|\d{3}-\d{2}-\d{4})$', str(inputssn)) :
            raise ValidationError(str(inputssn) + ': is not a valid SSN')
        return inputssn
'''

