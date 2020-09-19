from django.urls import path
from .views import vindex

urlpatterns = [
    path('', vindex.index, name='index'),
]