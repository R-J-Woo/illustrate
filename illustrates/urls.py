from django.urls import path
from rest_framework import routers
from .views import IllustViewSet

router = routers.SimpleRouter()
router.register('illustrates', IllustViewSet)

urlpatterns = router.urls
