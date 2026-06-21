from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
import datetime

def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        with open('messages.txt', 'a', encoding='utf-8') as f:
            f.write(f'--- {datetime.datetime.now()} ---\n')
            f.write(f'Имя: {name}\n')
            f.write(f'Email: {email}\n')
            f.write(f'Сообщение: {message}\n')
            f.write('\n')
        
        return HttpResponse('Спасибо! Ваше сообщение отправлено.')
    
    return render(request, 'blog/contacts.html')