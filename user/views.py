from django.shortcuts import render, redirect
from .admin import UserCreationForm
from django.contrib import messages
from Mental_health import classify
import statistics

list = []
sentiment_value_joy = []
sentiment_value_fear = []
sentiment_value_anger = []
sentiment_value_sadness = []
joy_value = 0
anger_value = 0
fear_value = 0
sadness_value = 0

def home(request):
    return render(request, 'user/home.html')

def about(request):
    return render(request, 'user/about.html')

def index(request):
    if request.method == 'POST':
        reason = request.POST.get('reason')
        sentiment = classify(reason)[0][0]
        if sentiment == 'joy':
            sentiment_value_joy.append(classify(reason)[0][1][0])
            joy_value = statistics.mean(sentiment_value_joy)
        if sentiment == 'anger':
            sentiment_value_anger.append(classify(reason)[0][1][0])
            anger_value = statistics.mean(sentiment_value_anger)
        if sentiment == 'fear':
            sentiment_value_fear.append(classify(reason)[0][1][0])
            fear_value = statistics.mean(sentiment_value_fear)
        if sentiment == 'sadness':
            sentiment_value_sadness.append(classify(reason)[0][1][0])
            sadness_value = statistics.mean(sentiment_value_sadness)
        list.insert(0,(sentiment));
        print(list)
        if len(list) > 5:
            del list[len(list)-1]
    context = {'list' : list}
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
