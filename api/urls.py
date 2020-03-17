from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from api.views import StudentsViewSet

router = routers.DefaultRouter()
router.register('rates', StudentsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
