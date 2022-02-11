from unicodedata import name
from django.urls import path
from .views import IndexView, EditView, DeleteView

urlpatterns = [
    path('', IndexView, name='index'),
    path('edit<int:id>/', EditView, name='edit'),
    path('delete/<int:id>/', DeleteView, name='delete'),
]
