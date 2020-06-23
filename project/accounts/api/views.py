from django.contrib.auth import get_user_model,login
from django.contrib.auth.models import User
from rest_framework import serializers,exceptions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.generics import (
    CreateAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)
from .serializers import (
    UserSerializer,
    # UserLoginSerializer
)


User = get_user_model()
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         if user:
    #             return Response(serializer.data, status=HTTP_200_OK)
    #     else:
    #         raise exceptions.ValidationError(serializer.errors)
    


















