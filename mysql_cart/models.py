from django.db import models
from django.core import validators
from django.urls import reverse

class SKUs(models.Model):
    sku = models.CharField(max_length=30, unique=True)
    mfg = models.CharField(max_length=50, default='', validators=[validators.MinLengthValidator(2, 'must be 2 characters or more.')])
    name = models.CharField(max_length=200, default='', validators=[validators.MinLengthValidator(2, 'must be 2 characters or more.')])
    desc  = models.TextField(default='')
    price = models.IntegerField(default=0)
    def get_absolute_url(self):
        # reverse is a custom in-built method that will send the user back to something if this model is utilized to make a record in a form
        # here the user will go back to the url "named" studentdetail and carry with it the argument of the current created private key or ID
        # that way after creation the user can see their own created stuff.
        return reverse('SKUdetail', kwargs={'pk':self.pk})


    class Meta:
        unique_together = [['sku', 'mfg']]

    def natural_key(self):
        return (self.sku, self.mfg)
