from .crud import CONFIG
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
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


def in_user_group(groups):
    if isinstance(groups, str):
        groups = [groups]  # Convert single group to a list
        print(format(groups))

    def check_group(user):
        print("I got here")
        return any(user.groups.filter(name=group).exists() for group in groups)

    return user_passes_test(check_group, reverse_lazy("auth:login"))
