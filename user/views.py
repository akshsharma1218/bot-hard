from django.shortcuts import render, redirect
from .admin import UserCreationForm
from django.contrib import messages


def home(request):
    return render(request, 'user/home.html')
    
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
