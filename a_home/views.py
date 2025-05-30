from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def home_view(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'home.html', context)

def create_item(request):
   if request.POST:
       name = request.POST.get('name')
       item = Item(name=name)
       item.save()
       return HttpResponse(f'<li class="text-8xl font-thin">{item.name}</li>')
   return redirect('home')