from rest_framework import serializers,exceptions
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email','address','phonenum']

        extrakwargs = {
            'password' : {'write_only':True}
        }
    def create(self,validated_data):
        User_obj = User(
            username = validated_data['username'],
            email = self.validated_data['email'],
            address = self.validated_data['address'],
            phonenum = self.validated_data['phonenum']
        )
        password = validated_data['password']
        User_obj.set_password(password)
        User_obj.save()
        return validated_data
