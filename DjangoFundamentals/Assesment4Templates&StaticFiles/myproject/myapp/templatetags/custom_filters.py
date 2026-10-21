from django import template

register = template.Library()

@register.filter
def truncate_words(value, count=3):
    words = value.split()
    return " ".join(words[:int(count)])