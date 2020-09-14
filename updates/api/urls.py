
from django.contrib import admin
from django.urls import path

from .views import UpdateModelListAPIView,UpdateModelDetailAPIView

urlpatterns = [
    path('<int:id>/', UpdateModelDetailAPIView.as_view() ),
    path('' , UpdateModelListAPIView.as_view()),
]
