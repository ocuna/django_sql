from django import template
import re
from django.contrib.humanize.templatetags.humanize import intcomma

#required to add custom filters into the library
register = template.Library()

def currency(dollars):
    dollars = round(float(dollars), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])

register.filter('currency', currency)

#basically it goes through the entire incoming value and replaces any "ate" with "8"
# this 'decorator' takes on the function filter() and supplies the argument - replaces what is below
@register.filter(name='n8iffy')
def n8iffy(value):
    #make sure this is going to be a string
    s = str(value)
    my_regex = 'ate'
    # replace anything matches my_regext with the number 8 in 's' string
    replaced = re.sub(my_regex,'8',s)
    return replaced
#register.filter('n8iffy', n8iffy)


#basically it goes through the entire incoming value and replaces any "ate" with "8"
# this 'decorator' takes on the function filter() and supplies the argument - replaces what is below
@register.filter(name='b5bg')
def b5bg(value,b5_colorcode):
    s = str(value)
    b5_colorcode = str(b5_colorcode)
    return '<span class="bg-' + b5_colorcode + ' fw-bold px-2">' + s + '</span>'

