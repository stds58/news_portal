
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author, User, Category
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm, ArtikullForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.http import HttpResponse


class PostsList(ListView):
    model = Post
    #ordering = '-datetime_in'
    queryset = Post.objects.filter(type__exact='NE').order_by('-datetime_in')
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    # def get(self, request):
    #     string = _('Все новости')
    #     context = {'string': string}
    #     return HttpResponse(render(request,'posts.html',context))

    # def get(self, request):
    #     models = Post.objects.all()
    #     context = {
    #         'models': models,
    #     }
    #     return HttpResponse(render(request,'posts.html',context))



class PostsListSearch(ListView):
    model = Post
    queryset = Post.objects.filter(type__exact='NE').order_by('-datetime_in')
    template_name = 'posts_search.html'
    context_object_name = 'posts_search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArtikullsListSearch(ListView):
    model = Post
    queryset = Post.objects.filter(type__exact='AR').order_by('-datetime_in')
    template_name = 'artikulls_search.html'
    context_object_name = 'artikulls_search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class ArtikullsList(ListView):
    model = Post
    queryset = Post.objects.filter(type__exact='AR').order_by('-datetime_in')
    template_name = 'artikulls.html'
    context_object_name = 'artikulls'
    paginate_by = 10


class ArtikullsDetail(DetailView):
    model = Post
    template_name = 'artikull.html'
    context_object_name = 'artikull'


class PostCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('sajt.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        author = Author.objects.filter(user_id = self.request.user).values('id')
        author_id = author.values_list('id')[0][0]
        post.author_id = author_id
        post.save()
        return super().form_valid(form)



class PostUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('sajt.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('sajt.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')


class ArtikullCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('sajt.add_post',)
    form_class = ArtikullForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'AR'
        post.save()
        return super().form_valid(form)

class ArtikullUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('sajt.change_post',)
    form_class = ArtikullForm
    model = Post
    template_name = 'post_edit.html'


class ArtikullDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('sajt.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')


class CategoryList(PostsList):
    model = Post
    template_name = 'news/category_List.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id = self.kwargs['pk'] )
        queryset = Post.objects.filter(category=self.category).order_by('-datetime_in')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user  = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'вы подписались на рассылку новостей категории '
    return render(request, 'news/subscribe.html', {'category': category, 'message': message})


@login_required
def unsubscribe(request, pk):
    user  = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)

    message = 'вы отписались от рассылки новостей категории '
    return render(request, 'news/unsubscribe.html', {'category': category, 'message': message})







