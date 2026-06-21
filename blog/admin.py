from django.contrib import admin
from .models import Article, ContactMessage

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'created_at')
    search_fields = ('title', 'short_description')
    list_filter = ('created_at',)
    fields = ('title', 'short_description', 'full_description', 'image')

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)