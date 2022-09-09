from django.urls import path
from .views import RegisterView, LoginView, ProfileView
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> e9ae3b523566da25597a16b68da2b86a584fd8e0

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),
<<<<<<< HEAD
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
]
>>>>>>> e9ae3b523566da25597a16b68da2b86a584fd8e0
