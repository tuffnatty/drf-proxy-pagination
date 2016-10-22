from django.conf.urls import url, include

from rest_framework import routers

from tests.views import TestViewSet


router = routers.DefaultRouter()
router.register(r'data', TestViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
