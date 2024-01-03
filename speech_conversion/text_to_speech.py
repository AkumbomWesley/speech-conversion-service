from gtts import gTTS
from pygame import mixer

def convert_text_to_speech(text, output_file_path):
    tts = gTTS(text, lang='en')
    tts.save(output_file_path)

def play_audio_file(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play