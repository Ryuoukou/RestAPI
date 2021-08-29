from django.db import router
from rest_framework import routers
from .api import TodoViewSet

router = routers.DefaultRouter()
router.register('api/restapi', TodoViewSet, 'restapi')


urlpatterns = router.urls