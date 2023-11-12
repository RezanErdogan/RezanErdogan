from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import logging

def upload_to_youtube(video_path, title="Dein Video Titel", description="Deine Videobeschreibung", category_id="22", privacy_status="public"):
    try:
        # Authentifizierung und Erstellen eines YouTube-Service-Objekts
        scopes = ["https://www.googleapis.com/auth/youtube.upload"]
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes)
        credentials = flow.run_console()
        youtube = build("youtube", "v3", credentials=credentials)

        # Erstellen des Request-Body und Hochladen des Videos
        request_body = {
            "snippet": {
                "categoryId": category_id,
                "description": description,
                "title": title
            },
            "status": {
                "privacyStatus": privacy_status
            }
        }

        media_file = MediaFileUpload(video_path)

        request = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media_file
        )

        response = request.execute()

        logging.info(f"Video erfolgreich hochgeladen. Video ID: {response.get('id')}")
        return response.get("id")
    except Exception as e:
        logging.error(f"Fehler beim Hochladen des Videos: {e}")
        return None
