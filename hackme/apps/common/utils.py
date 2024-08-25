from .crud import CONFIG
import re
import math
from urllib.parse import urlparse, parse_qs
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

    def check_group(user):
        return any(user.groups.filter(name=group).exists() for group in groups)

    return user_passes_test(check_group, reverse_lazy("auth:login"))


def estimate_reading_time(text, average_wpm=100):
    if average_wpm <= 0:
        raise ValueError("Average words per minute must be greater than zero.")

    # Count the number of words in the text
    word_count = len(text.split())

    # Calculate the estimated reading time
    reading_time_minutes = word_count / average_wpm

    return math.ceil(reading_time_minutes)


def is_youtube_url(url):

    parsed_url = urlparse(url)
    youtube_patterns = [
        r'^(www\.)?youtube\.com$',  # www.youtube.com or youtube.com
        r'^m\.youtube\.com$',       # m.youtube.com (mobile)
        r'^youtu\.be$',             # youtu.be (shortened URLs)
    ]
    # Check if the domain matches any of the YouTube patterns
    if any(re.match(pattern, parsed_url.netloc) for pattern in youtube_patterns):
        return True

    return False


def convert_to_embed_url(youtube_url):
    parsed_url = urlparse(youtube_url)

    if parsed_url.netloc in ['www.youtube.com', 'youtube.com'] and parsed_url.path.startswith('/embed/'):
        return youtube_url

    if parsed_url.netloc in ['www.youtube.com', 'youtube.com', 'm.youtube.com'] and parsed_url.path == '/watch':
        query_params = parse_qs(parsed_url.query)
        video_id = query_params.get('v')
        if video_id:
            return f"https://www.youtube.com/embed/{video_id[0]}"
    return None  # If the URL is not a valid YouTube video link


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


def is_user_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
