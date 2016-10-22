from django.conf import settings

from rest_framework.pagination import BasePagination
from rest_framework.settings import import_from_string

__version__ = '0.1.0'


class ProxyPagination(BasePagination):
    """
    A simple configurable pagination proxy.
    """
    default_pager = import_from_string(settings.PROXY_PAGINATION_DEFAULT,
                                       'PROXY_PAGINATION_DEFAULT')
    pager_query_param = settings.PROXY_PAGINATION_PARAM or 'pager'
    mapping = {alias: import_from_string(path, 'PROXY_PAGINATION_MAPPING')
               for alias, path in settings.PROXY_PAGINATION_MAPPING.items()}

    def paginate_queryset(self, queryset, request, view=None):
        alias = request.query_params.get(self.pager_query_param)
        self.pager = self.mapping.get(alias, self.default_pager)()
        return self.pager.paginate_queryset(queryset, request, view=view)

    def get_paginated_response(self, data):
        return self.pager.get_paginated_response(data)

    def to_html(self):
        return self.pager.to_html()

    def get_results(self, data):
        return self.pager.get_results(data)

    def get_fields(self, view):
        return self.pager.get_fields(view)

    def get_schema_fields(self, view):
        return self.pager.get_schema_fields(view)
