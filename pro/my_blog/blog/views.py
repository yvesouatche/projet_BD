from django.shortcuts import render
from .models import Enfant

def home(request):
    list_articles = Enfant.objects.all()
    return render(request,"index.html",{})
