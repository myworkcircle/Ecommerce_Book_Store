from rest_framework import serializers,exceptions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)
from .models import (
    Book,
    BookCategories,
)
from .serializers import (
    BookSerializer,
    BookCategoriesSerializer,
)



class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

        

class BookListAPIView(ListAPIView):
    serializer_class =  BookSerializer
    queryset = Book.objects.all()

class BookRetreiveView(ListAPIView): 
    serializer_class = BookSerializer
    def get_queryset(self,**kwargs):
        data = self.kwargs['category_id']
        object1 = Book.objects.filter(category_id=data)
        return object1


class BookCategoryAPIView(CreateAPIView):
    serializer_class =  BookCategoriesSerializer
    queryset = BookCategories.objects.all()
















