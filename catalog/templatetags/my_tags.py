
from django.conf import settings

from django import template

register = template.Library()

@register.filter()
def media_filter(path):
    if path:
        return f"media/{path}"
    return "#"


def media_filter(path: str):
    if path:
        return f"{settings.MEDIA_URL}{path}"
    return ""
