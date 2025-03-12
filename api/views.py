import googleapiclient
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google_auth_oauthlib.flow import Flow
from django.conf import settings
from googleapiclient.http import MediaIoBaseUpload
from google.oauth2.credentials import Credentials
import logging
import io
from googleapiclient.discovery import build
import googleapiclient.discovery
from googleapiclient.http import MediaIoBaseDownload


logger = logging.getLogger(__name__)

def google_login(request):
    flow = Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/drive.file'],
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    auth_url, _ = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
        prompt='consent'
    )
    return JsonResponse({'auth_url': auth_url})

def google_callback(request):
    try:
        code = request.GET.get('code')
        if not code:
            return JsonResponse({"error": "Authorization code missing"}, status=400)

        flow = Flow.from_client_secrets_file(
            'client_secret.json',
            scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/drive.file'],
            redirect_uri=settings.GOOGLE_REDIRECT_URI
        )

        flow.fetch_token(code=code)  # Exchange code for token
        credentials = flow.credentials
        request.session['google_access_token'] = credentials.token

        return JsonResponse({'token': credentials.token})  # Return only the token

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def upload_file_to_drive(request):
    access_token = request.headers.get('Authorization')
    if not access_token or not access_token.startswith("Bearer "):
        return JsonResponse({"error": "Access token missing"}, status=401)

    access_token = access_token.split("Bearer ")[-1]

    if 'file' not in request.FILES:
        return JsonResponse({"error": "No file uploaded"}, status=400)

    uploaded_file = request.FILES['file']

    file_stream = io.BytesIO(uploaded_file.read())
    media = MediaIoBaseUpload(file_stream, mimetype=uploaded_file.content_type)

    credentials = Credentials(token=access_token)
    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {'name': uploaded_file.name}
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    return JsonResponse({'file_id': file.get('id')})

def list_google_drive_files(request):
    try:
        access_token = request.headers.get('Authorization')
        if not access_token or not access_token.startswith("Bearer "):
            return JsonResponse({"error": "Access token missing"}, status=401)

        access_token = access_token.split("Bearer ")[-1]

        credentials = Credentials(token=access_token)
        service = googleapiclient.discovery.build('drive', 'v3', credentials=credentials)

        files = service.files().list().execute().get("files", [])

        return JsonResponse({"files": files})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@csrf_exempt
def download_google_drive_file(request):
    try:
        # Get access token and file ID
        access_token = request.headers.get('Authorization')
        file_id = request.GET.get("file_id")

        if not access_token or not file_id:
            return JsonResponse({"error": "Access token or file ID missing"}, status=400)

        access_token = access_token.split("Bearer ")[-1]
        credentials = Credentials(token=access_token)
        service = googleapiclient.discovery.build('drive', 'v3', credentials=credentials)

        # Get file metadata
        file_metadata = service.files().get(fileId=file_id, fields="name, mimeType").execute()
        file_name = file_metadata.get("name", f"downloaded_{file_id}")
        mime_type = file_metadata.get("mimeType", "application/octet-stream")

        # Download file into memory
        request_file = service.files().get_media(fileId=file_id)
        file_stream = io.BytesIO()
        downloader = MediaIoBaseDownload(file_stream, request_file)
        done = False
        while not done:
            _, done = downloader.next_chunk()

        file_stream.seek(0)  # Move cursor to the beginning

        # Return file as an HTTP response for direct download
        response = HttpResponse(file_stream, content_type=mime_type)
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
