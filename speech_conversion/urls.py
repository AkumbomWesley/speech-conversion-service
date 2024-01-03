from django.urls import path
from .views import text_to_speech, speech_to_text

url_patterns = [
    path('text-to-speech/', text_to_speech, name='text-to-speech'),
    path('speech_to_text/', speech_to_text, name='speech_to-text'),
]