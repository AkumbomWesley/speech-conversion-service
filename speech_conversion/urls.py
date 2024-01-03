from django.urls import path
from .views import text_to_speech, speech_to_text

urlpatterns = [
    path('text-to-speech/', text_to_speech, name='text_to_speech'),
    path('speech-to-text/', speech_to_text, name='speech_to_text'),
]
