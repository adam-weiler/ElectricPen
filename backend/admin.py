from django.contrib import admin
from backend.models import Article, Topic, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'slug', 'status','created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Topic)
admin.site.register(Comment)