import openai
import logging
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

def generate_text(prompt):
    try:
        openai.api_key = 'DEIN_API_SCHLÜSSEL'
        response = openai.Completion.create(prompt=prompt, max_tokens=100)
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        logging.error(f"Fehler bei der Textgenerierung: {e}")
        return None