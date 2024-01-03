from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .text_to_speech import convert_text_to_speech, play_audio_file
from .speech_to_text import convert_speech_to_text

@csrf_exempt
def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        output_file_path = 'output.mp3'
        convert_text_to_speech(text, output_file_path)
        return JsonResponse({"audio_file": output_file_path})
    
    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def speech_to_text(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio')
        audio_file_path = 'audio.wav'
        with open(audio_file_path, 'wb') as f:
            for chunk in audio_file.chunks():
                f.write(chunk)
        text = convert_speech_to_text(audio_file_path)
        return JsonResponse({'text': text}) 