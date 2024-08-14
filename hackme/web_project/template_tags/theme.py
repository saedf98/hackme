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


@register.simple_tag
def random_text_color():
    text_colors = [
        'text-primary', 'text-secondary', 'text-success',
        'text-danger', 'text-warning', 'text-info',
        'text-dark'
    ]
    return random.choice(text_colors)


@register.filter(name='remove_before_vertical_bar')
def remove_before_vertical_bar(value):
    try:
        value = str(value)
        parts = value.split('|', 1)
        return parts[1].strip() if len(parts) > 1 else value
    except ValueError:
        return value


@register.filter(name='capitalize_after_remove_vertical_bar')
def capitalize_after_remove_vertical_bar(value):
    word = remove_before_vertical_bar(value)
    return word[0].upper() + word[1:]


@register.filter
def number_to_words(value):
    try:
        # Convert number to word format
        number = int(value)
        number_word = p.number_to_words(number)
        # print(number_word)
        return number_word[0].upper() + number_word[1:]
        # return number_word
    except (ValueError, TypeError):
        return "Invalid number"


@register.filter(name='convert_minutes')
def convert_minutes(duration_minutes):
    if duration_minutes < 0:
        raise ValueError("Duration must be a non-negative integer.")

    if duration_minutes >= 60:
        hours = duration_minutes // 60
        minutes = duration_minutes % 60
        if minutes == 0:
            return f"{hours} hour(s)"
        return f"{hours} hour(s) {minutes} minute(s)"
    else:
        return f"{duration_minutes} minute(s)"


@register.filter(name='add_number')
def add_number(value, arg):
    total = int(value) + int(arg)
    print(value, arg, total)
    return total


@register.filter
def total_duration(lessons):
    return sum(lesson.duration for lesson in lessons)


@register.filter
def total_lessons(lessons):
    return sum(1 for lesson in lessons)


@register.filter
def total_completed_lessons(lessons):
    return sum(lesson.duration.completed for lesson in lessons)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
