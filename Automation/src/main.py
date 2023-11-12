from content_generator import generate_text
from video_creator import create_video
from text_to_speech import convert_text_to_speech
from speech_to_text import convert_speech_to_text
from youtube_uploader import upload_to_youtube
from tiktok_uploader import upload_video_to_tiktok
import logging

def main():
    prompt = "Nachrichtenartikel über..."
    text = generate_text(prompt)
    if text:
        video_path = create_video(text, "background.jpg")  # Angenommen, Sie haben ein Hintergrundbild
        if video_path:
            audio_path = convert_text_to_speech(text)
            if audio_path:
                subtitle_path = convert_speech_to_text(audio_path)
                if subtitle_path:
                    # Upload to YouTube
                    upload_to_youtube(video_path, audio_path, subtitle_path)
                    # Upload to TikTok
                    upload_video_to_tiktok(video_path)
                else:
                    logging.error("Fehler bei der Erstellung von Untertiteln")
            else:
                logging.error("Fehler bei der Vertonung")
        else:
            logging.error("Fehler bei der Videoerstellung")
    else:
        logging.error("Fehler bei der Textgenerierung")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
