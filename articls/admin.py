from django.contrib import admin
from .models import Article, Comments

# Register your models here.
# Class CommentInline()
class CommentInLine(admin.TabularInline):
    model = Comments
    extra = 0

class ArticlAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(Article, ArticlAdmin)
admin.site.register(Comments)