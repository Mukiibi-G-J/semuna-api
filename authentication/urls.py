from django.urls import path
from .views import BlackListTokenView, CustomerUserCreate
from django.urls import path
from .views import  MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

app_name='authentication'

urlpatterns = [
   
    path('register', CustomerUserCreate.as_view(), name='create_user') ,
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/', BlackListTokenView.as_view(), name='blacklist'),
    
]





