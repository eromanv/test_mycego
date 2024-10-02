from django.urls import path
from .views import file_list_view, download_file

urlpatterns = [
    path('', file_list_view, name='file_list'),
    path('download/<str:public_key>/<path:file_path>/', download_file, name='download_file'),
]
