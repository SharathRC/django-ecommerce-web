from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    
    
    return render(request, 'vendor_detail.html', context)

def my_account(request):
    return render(request, 'my_account.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            
            UserProfile.objects.create(user=user)
            
            return redirect('homepage')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})