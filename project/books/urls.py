
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from .views import(
    BookCreateAPIView,
    BookListAPIView,
    BookCategoryAPIView,
    BookRetreiveView
)

urlpatterns = [
    path('create/', BookCreateAPIView.as_view(),name="create"),
    path('list/',BookListAPIView.as_view(),name="list"),
    path('retreive/<category_id>/',BookRetreiveView.as_view(),name="retreive"),
    path('categorylist/',BookCategoryAPIView.as_view(),name="category"),
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
