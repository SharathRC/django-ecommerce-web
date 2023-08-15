from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Item

from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            
            new_user.save()
            
            return render(request, 'account/register_done.html', {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
        
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
@csrf_exempt
def item_list(request):
    if request.method == 'GET':
        context = {
            'items': Item.objects.all(),
        }
        return render(request, "home-page/home-page.html", context)
    
    if request.method == 'POST':
        id = request.POST.get('id')
        if id == '':
            item = Item.objects.create(
                title = request.POST.get('title'),
                price = request.POST.get('price')
            )
            item.save()
            return redirect('item_list')
        else:
            item = Item.objects.get(id=id)
            item.title = request.POST.get('title')
            item.price = request.POST.get('price')
            item.save()
            return redirect('item_list')