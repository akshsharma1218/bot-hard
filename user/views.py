from django.shortcuts import render, redirect
from .admin import UserCreationForm
from django.contrib import messages
# from Mental_health import pred
import statistics
from django.contrib.auth.decorators import login_required

list = []
sentiment_value_joy = []
sentiment_value_fear = []
sentiment_value_anger = []
sentiment_value_sadness = []
joy_value = 0
anger_value = 0
fear_value = 0
sadness_value = 0

@login_required
def home(request):
    user = request.user
    context = {'n':range(20), 'user':user}
    return render(request, 'user/home.html', context)

def about(request):
    return render(request, 'user/about.html')

def index(request):
    if request.method == 'POST':
        reason = request.POST.get('reason')
        # sentiment = pred(reason)
        # list.insert(0,(sentiment))
        # print(list)
        # if len(list) > 5:
        #     del list[len(list)-1]
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
