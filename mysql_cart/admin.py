from django.contrib import admin
from mysql_cart.models import SKUs

# another way to have the employee Admin display admin records
class SKUsAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(SKUs,SKUsAdmin)
# Register your models here.
