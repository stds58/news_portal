from django.views.generic import ListView, DetailView
from .models import Post, Author
from datetime import datetime

class PostsList(ListView):
    model = Post
    ordering = '-datetime_in'
    template_name = 'posts.html'
    context_object_name = 'posts'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['next_sale'] = Post.avtor()
    #     return context


class PostsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'