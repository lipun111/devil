from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    form = PostForm()
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = PostForm()
    return render(request, 'users/profile.html', {'form':form})
