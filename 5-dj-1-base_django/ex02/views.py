import os
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from .forms import InputForm

def index(request):
    form = InputForm()
    history:list[str] = []

    if os.path.exists(settings.LOG_FILE_PATH):
        with open(settings.LOG_FILE_PATH, 'r') as file:
            history = [line.strip() for line in file.readlines()]

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['text']
            timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"{timestamp} - {input_text}"

            with open(settings.LOG_FILE_PATH, 'a') as file:
                file.write(log_entry + '\n')
            history.append(log_entry)

    return render(request, 'ex02/index.html', {'form': form, 'history': history})
