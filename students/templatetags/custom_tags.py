from django import template

register = template.Library()

@register.simple_tag
def get_half_content(description):
    total = len(description)
    half = total//2
    content = description[:half]
    return content
