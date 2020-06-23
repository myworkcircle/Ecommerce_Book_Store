from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserCreateAPIView,
    # UserLoginView
)

urlpatterns=[
    path('login/',obtain_auth_token,name='login'),
    # path('login/',UserLoginView.as_view(),name='login'),
    path('register/',UserCreateAPIView.as_view(),name='register'),
]

# curl -X POST http://127.0.0.1:8000/accounts/api/login/?username=s&password=s -H 'Authorization: Token  76a8753f29e75e313d8ed8f746474142456d752b '