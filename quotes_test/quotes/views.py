from django.shortcuts import render, HttpResponse
from .models import Quote
import random

# Create your views here.
def home(request):
    quotes = list(Quote.objects.all())
    random_quote = random.choice(quotes) if quotes else None
    return render(request, 'home.html', {'quote' : random_quote})