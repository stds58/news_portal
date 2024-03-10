from django.contrib import admin
from .models import Post, Category, Author,PostCategory, Comment
from modeltranslation.admin import \
    TranslationAdmin  # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)


# Регистрируем модели для перевода в админке
class CategoryAdmin(TranslationAdmin):
    model = Category

class MyModelAdmin(TranslationAdmin):
    model = Post

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)

