from django.urls import path
from .views import CustomUserCreate, BlacklistTokenView, CustomTokenObtainPairView

# Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenView.as_view(),
         name="blacklist"),
    # Authentication
    path('api-token/', CustomTokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
]
