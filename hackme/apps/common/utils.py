from django.conf import settings
from django.urls import reverse
from .crud import CONFIG


# get_config_value('common.actions')
def get_config_value(key):
    keys = key.split('.')
    value = CONFIG
    try:
        for k in keys:
            value = value[k]
    except KeyError:
        value = None
    return value


def get_url(url_name):
    base_url = settings.BASE_URL
    return base_url + reverse(url_name)
