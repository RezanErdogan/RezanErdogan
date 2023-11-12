from google.cloud import texttospeech
import logging

def convert_text_to_speech(text, language_code="de-DE", voice_name="de-DE-Standard-A"):
    try:
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(language_code=language_code, name=voice_name)
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

        response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
        audio_path = 'output_audio.mp3'
        with open(audio_path, 'wb') as out_file:
            out_file.write(response.audio_content)
        return audio_path
    except Exception as e:
        logging.error(f"Fehler bei der Text-zu-Sprache-Umwandlung: {e}")
        return None