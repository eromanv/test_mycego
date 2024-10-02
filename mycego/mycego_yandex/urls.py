from django.urls import path
from .views import file_list_view, download_file

urlpatterns = [
    path('', file_list_view, name='file_list'),
  ]
