import random
import inflect
from word2number import w2n
from django.utils.safestring import mark_safe
from django import template
from apps.common.utils import get_config_value
from web_project.template_helpers.theme import TemplateHelper

register = template.Library()
p = inflect.engine()

# Register tags as an adapter for the Theme class usage in the HTML template


@register.simple_tag
def get_theme_variables(scope):
    return mark_safe(TemplateHelper.get_theme_variables(scope))


@register.filter(name='get_config')
def get_config(value):
    return get_config_value(value)


@register.filter
def in_user_group(user, group_name):
    if user.is_authenticated:
        return user.groups.filter(name=group_name).exists()
    return False


@register.filter(name='capitalize_first')
def capitalize_first(value):
    if isinstance(value, str):
        return value.capitalize()
    return value


@register.filter
def truncate_71(value):
    """Returns the first 71 characters of the value, appending '...' if truncated"""
    if len(value) > 71:
        return value[:68] + '...'
    return value[:71]


@register.simple_tag
def random_bg_label_color():
    colors = [
        'bg-label-primary', 'bg-label-secondary', 'bg-label-success',
        'bg-label-danger', 'bg-label-warning', 'bg-label-info',
        'bg-label-dark'
    ]
    return random.choice(colors)


@register.filter(name='remove_before_vertical_bar')
def remove_before_vertical_bar(value):
    try:
        value = str(value)
        parts = value.split('|', 1)
        return parts[1].strip() if len(parts) > 1 else value
    except ValueError:
        return value


@register.filter
def number_to_words(value):
    try:
        # Convert number to word format
        number = int(value)
        number_word = p.number_to_words(number)
        print(number_word)
        return number_word[0].upper() + number_word[1:]
        # return number_word
    except (ValueError, TypeError):
        return "Invalid number"
