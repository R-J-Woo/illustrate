from django.urls import path
from rest_framework import routers
from .views import IllustViewSet, like_illustrate

router = routers.SimpleRouter()
router.register('illustrates', IllustViewSet)

urlpatterns = router.urls + [
    path('like/<int:pk>/', like_illustrate),
]
