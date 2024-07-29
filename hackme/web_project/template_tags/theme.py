from django.utils.safestring import mark_safe
from django import template
from apps.common.utils import get_config_value
from web_project.template_helpers.theme import TemplateHelper

register = template.Library()


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
