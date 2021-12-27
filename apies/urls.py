# Standard imports
from django.urls import path
from rest_framework import views

# Local imports
from .views import (BookAPi, SectionApi, AuthorApi)

urlpatterns = [
    path('books/', BookAPi.as_view(), name="books"),
    path('sections/', SectionApi.as_view(), name="section"),
    path('authors/', AuthorApi.as_view(), name="author"),
]
