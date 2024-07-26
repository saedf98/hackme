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
