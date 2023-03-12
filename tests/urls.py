from django.urls import include, re_path

from rest_framework import routers

from tests.views import TestViewSet


router = routers.DefaultRouter()
router.register(r'data', TestViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
