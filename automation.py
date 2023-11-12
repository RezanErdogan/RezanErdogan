from openai import OpenAIAPI
from moviepy.editor import VideoClip, TextClip, CompositeVideoClip, ImageClip
from google.cloud import texttospeech, speech_v1p1beta1 as speech
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

# Schritt 1: Textgenerierung mit GPT-3 (oder ähnlichem Modell)
openai = OpenAIAPI(api_key='DEIN_API_SCHLÜSSEL')
text_prompt = 'Nachrichtenartikel über...'
generated_text = openai.generate_text(prompt=text_prompt)

# Schritt 2: Videoerstellung mit MoviePy
def make_video():
    text_clip = TextClip(generated_text, fontsize=24, color='white')
    final_clip = CompositeVideoClip([text_clip])
    return final_clip

video = make_video()
video_path = "output_video.mp4"
video.write_videofile(video_path, codec='libx264', audio_codec='aac')

# Schritt 3: Vertonung mit Google Text-to-Speech
client_tts = texttospeech.TextToSpeechClient()
synthesis_input = texttospeech.SynthesisInput(text=generated_text)
voice_params = texttospeech.VoiceSelectionParams(language_code="de-DE", name="de-DE-Standard-A")
response = client_tts.synthesize_speech(input=synthesis_input, voice=voice_params)

# Speichere die vertonte Sprachdatei
audio_path = 'output_audio.mp3'
with open(audio_path, 'wb') as out_file:
    out_file.write(response.audio_content)

# Schritt 4: Untertitelung mit Google Cloud Speech-to-Text
client_stt = speech.SpeechClient()
audio_config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="de-DE",
)

with open(audio_path, 'rb') as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
response_stt = client_stt.recognize(config=audio_config, audio=audio)

# Extrahiere den transkribierten Text aus der Antwort
transcribed_text = response_stt.results[0].alternatives[0].transcript

# Schritt 5: Speichere den transkribierten Text als Untertitel
subtitle_path = 'output_subtitle.srt'
with open(subtitle_path, 'w') as subtitle_file:
    subtitle_file.write("1\n00:00:00,000 --> 00:00:10,000\n" + transcribed_text)

# Optional: Schritt 6 - Plattform-Upload
# Hier könntest du den Code für den Upload auf YouTube Shorts oder TikTok integrieren.
# Beachte, dass dies sehr plattformabhängig ist und spezifische APIs erfordert.

# Beispiel für YouTube Upload mit google-auth und google-auth-oauthlib
# Weitere Informationen: https://developers.google.com/youtube/registering_an_application
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    creds = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=creds)

youtube = authenticate()

def upload_to_youtube(video_path, audio_path, subtitle_path):
    # Lade das Video hoch
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "categoryId": "22",  # Kategorie für Menschen und Blogs
                "description": "Beschreibung deines Videos hier",
                "title": "Titel deines Videos hier",
            },
            "status": {"privacyStatus": "public"},  # Setze auf "private" für nicht gelistete Videos
        },
        media_body=MediaFileUpload(video_path),
    )
    response = request.execute()

    # Setze die Videoid für Untertitelung
    video_id = response["id"]

    # Lade die vertonte Sprachdatei hoch
    audio_request = youtube.captions().insert(
        part="snippet",
        body={
            "snippet": {
                "videoId": video_id,
                "language": "de",
                "name": "Deutsch",
            },
        },
        media_body=MediaFileUpload(audio_path),
    )
    audio_response = audio_request.execute()

    # Setze die CaptionId für Untertitelung
    caption_id = audio_response["id"]

    # Lade die Untertitel hoch
    subtitle_request = youtube.captions().update(
        part="snippet",
        body={
            "id": caption_id,
            "snippet": {
                "videoId": video_id,
                "language": "de",
                "name": "Deutsch",
            },
        },
        media_body=MediaFileUpload(subtitle_path),
    )
    subtitle_response = subtitle_request.execute()

# Rufe die Upload-Funktion auf
upload_to_youtube(video_path, audio_path, subtitle_path)
