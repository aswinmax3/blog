from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Blog, Post
from .forms import BlogForm, PostForm


class HomeView(ListView):
    model = Post
    template_name = 'blogs/home.html'
    context_object_name = 'posts'


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/blog_form.html'
    success_url = reverse_lazy('blogs:home')


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogs/post_form.html'
    success_url = reverse_lazy('blogs:home')


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blogs/post_form.html'
    success_url = reverse_lazy('blogs:home')