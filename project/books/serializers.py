from rest_framework import serializers,exceptions
from .models import (
    Book,
    BookCategories,
)
from django.db.models import Q
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def create(self,validated_data):
        obj = Book(**validated_data)
        obj.save()

class BookCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategories
        fields = '__all__'



    
