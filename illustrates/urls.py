from django.urls import path
from rest_framework import routers
from .views import IllustViewSet, like_illustrate, ReviewViewSet

router = routers.SimpleRouter()
router.register('illustrates', IllustViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = router.urls + [
    path('like/<int:pk>/', like_illustrate),
]
