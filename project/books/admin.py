from django.contrib import admin
from .models import (
    Book,
    BookCategories,
)
to_register = (
    Book,
    BookCategories,
)
admin.site.register(to_register)