from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserListAPIView, UserRetrieveAPIView, UserCreateAPIView, UserUpdateAPIView, \
    UserDestroyAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('register/', UserCreateAPIView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

    # токен
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
