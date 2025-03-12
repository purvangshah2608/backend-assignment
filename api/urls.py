from django.urls import path
from .views import google_login, google_callback, upload_file_to_drive, list_google_drive_files, download_google_drive_file


urlpatterns = [
    path('auth/login/', google_login, name='google_login'),
    path('auth/callback/', google_callback, name='google_callback'),
    path('drive/upload/', upload_file_to_drive, name='upload_file_to_drive'),
    path('drive/files/', list_google_drive_files, name='list_google_drive_files'),
    path('drive/download/', download_google_drive_file, name='download_google_drive_file'),
]
