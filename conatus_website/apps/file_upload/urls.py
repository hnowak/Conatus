from django.contrib.auth import views as auth_views
from django.urls import path

from .views import FileUpload

app_name = 'file_upload'
urlpatterns = [
    path('profile/upload/', FileUpload.as_view(), name='file_upload'),
]