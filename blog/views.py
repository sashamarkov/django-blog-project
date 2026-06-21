from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article
from .forms import ContactMessageForm

def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

def contacts(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contacts_success'))
    else:
        form = ContactMessageForm()
    
    return render(request, 'blog/contacts.html', {'form': form})

def contacts_success(request):
    return render(request, 'blog/contacts_success.html')