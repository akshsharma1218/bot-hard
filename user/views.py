from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .admin import UserCreationForm
from django.contrib import messages
from Mental_health import pred
from .models import *
import statistics
import secrets

list = []

@login_required
def home(request):
    user = request.user
    context = {'n':range(20), 'user':user}
    return render(request, 'user/home.html', context)

def about(request):
    return render(request, 'user/about.html')

@login_required
def index(request):
    questions = Questions.objects.get(id='1')
    if request.method == 'POST':
        reason = request.POST.get('reason')
        sentiment = pred(reason)
        list.insert(0,(sentiment))
        user = request.user
        list.append(sentiment)
        user.list.append(sentiment)
        user.save()
        if sentiment == 'joy':
            question = questions.question_joy
            que      = secrets.choice(question)
            # que      = "happy"
        elif sentiment == 'sadness':
            question = questions.question_sad
            que      = secrets.choice(question)
            # que      = "sad"
        elif sentiment == 'fear':
            question = questions.question_fear
            que      = secrets.choice(question)
            # que      = "fear"
        elif sentiment == 'anger':
            question = questions.question_anger
            que      = secrets.choice(question)
            # que      = "anger"
        else:
            que = "ok... tell us some more"
    else:
        que = "How are you feeling?"
    context = {'que' : que,'list':list }
    return render(request, 'user/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request,'user/register.html',context)
