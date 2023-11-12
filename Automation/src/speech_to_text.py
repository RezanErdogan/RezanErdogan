from google.cloud import speech
import logging

def convert_speech_to_text(audio_path):
    try:
        client = speech.SpeechClient()
        with open(audio_path, 'rb') as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="de-DE",
        )

        response = client.recognize(config=config, audio=audio)
        transcript = response.results[0].alternatives[0].transcript
        subtitle_path = 'output_subtitle.srt'
        with open(subtitle_path, 'w') as subtitle_file:
            subtitle_file.write(transcript)
        return subtitle_path
    except Exception as e:
        logging.error(f"Fehler bei der Sprach-zu-Text-Umwandlung: {e}")
        return None
