from django.conf import settings

from rest_framework.pagination import BasePagination
from rest_framework.settings import import_from_string

__version__ = '0.2.0'


class ProxyPagination(BasePagination):
    """
    A simple configurable pagination proxy.
    """
    default_pager = import_from_string(settings.PROXY_PAGINATION_DEFAULT,
                                       'PROXY_PAGINATION_DEFAULT')
    pager_query_param = settings.PROXY_PAGINATION_PARAM or 'pager'
    pager_mapping = {alias: import_from_string(path, 'PROXY_PAGINATION_MAPPING')
                     for alias, path in settings.PROXY_PAGINATION_MAPPING.items()}

    @property
    def display_page_controls(self):
        return self.pager.display_page_controls

    @display_page_controls.setter
    def display_page_controls(self, value):
        self.pager.display_page_controls = value

    @property
    def template(self):
        return self.pager.template

    @template.setter
    def template(self, value):
        self.pager.template = value

    def __init__(self):
        self.pager = self.default_pager()

    def paginate_queryset(self, queryset, request, view=None):
        alias = request.query_params.get(self.pager_query_param)
        self.pager = self.pager_mapping.get(alias, self.default_pager)()
        return self.pager.paginate_queryset(queryset, request, view=view)

    def get_paginated_response(self, data):
        return self.pager.get_paginated_response(data)

    def to_html(self):
        return self.pager.to_html()

    def get_results(self, data):
        return self.pager.get_results(data)

    def get_fields(self, view):
        return self.pager.get_fields(view)

    def get_html_context(self):
        return self.pager.get_html_context()

    def get_schema_fields(self, view):
        return self.pager.get_schema_fields(view)
