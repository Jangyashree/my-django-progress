from django import template

register=template.Library()

@register.filter()
def capitalize(value):
    return value.capitalize()

@register.filter('split')
def splitting(value,delemetor):
    return value.split(delemetor)

#register.filter('capitalize',capitalize)
#register.filter('split',splitting
