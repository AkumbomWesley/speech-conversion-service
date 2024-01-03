import speech_recognition as sr 

def convert_speech_to_text(audio_file_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text