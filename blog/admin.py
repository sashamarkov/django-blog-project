from django.contrib import admin
from .models import Article, ContactMessage

admin.site.register(Article)
admin.site.register(ContactMessage)