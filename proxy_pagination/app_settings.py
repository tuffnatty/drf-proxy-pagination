from django.conf import settings
from rest_framework.settings import APISettings as _APISettings


USER_SETTINGS = getattr(settings, "PROXY_PAGINATION", None)

DEFAULTS = {
    'DEFAULT': 'rest_framework.pagination.LimitOffsetPagination',
    'MAPPING': {
        'cursor': 'rest_framework.pagination.CursorPagination',
    },
    'PARAM': 'pager',
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = (
    'DEFAULT',
)

# List of settings that have been removed
REMOVED_SETTINGS = ()


class APISettings(_APISettings):  # pragma: no cover
    pass


api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
