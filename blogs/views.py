from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Blog, Post
from .forms import BlogForm, PostForm


def home(request):
    blogs = Blog.objects.all()
    posts = Post.objects.all().order_by('-date_added')

    return render(request, 'blogs/home.html', {
        'blogs': blogs,
        'posts': posts,
    })


@login_required
def new_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    else:
        form = BlogForm()

    return render(request, 'blogs/blog_form.html', {'form': form})


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    else:
        form = PostForm()

    return render(request, 'blogs/post_form.html', {'form': form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    else:
        form = PostForm(instance=post)

    return render(request, 'blogs/post_form.html', {
        'form': form,
        'post': post,
    })


@login_required
def analytics(request):
    blogs = Blog.objects.all()
    posts = Post.objects.all().order_by('-date_added')

    return render(request, 'blogs/analytics.html', {
        'blogs': blogs,
        'posts': posts,
    })


@login_required
def settings_view(request):
    return render(request, 'blogs/settings.html')


@login_required
def profile(request):
    return render(request, 'blogs/profile.html')


@login_required
def messages_view(request):
    return render(request, 'blogs/messages.html')


@login_required
def notifications(request):
    return render(request, 'blogs/notifications.html')

from django.shortcuts import render

def total_views(request):
    return render(request, 'blogs/total_views.html')

def total_likes(request):
    return render(request, 'blogs/total_likes.html')

from django.shortcuts import render

def analytics(request):
    return render(request, 'blogs/analytics.html')

def profile(request):
    return render(request, 'blogs/profile.html')

def notifications(request):
    return render(request, 'blogs/notifications.html')

from django.shortcuts import render
from .models import Post


def activity_views(request):
    posts = Post.objects.all().order_by('-date_added')
    return render(request, 'blogs/activity_views.html', {'posts': posts})


def activity_likes(request):
    posts = Post.objects.all().order_by('-date_added')
    return render(request, 'blogs/activity_likes.html', {'posts': posts})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Post


def analytics(request):
    posts = Post.objects.all()

    total_posts = posts.count()
    total_blogs = Blog.objects.count()
    total_views = sum(post.views for post in posts)
    total_likes = sum(post.likes for post in posts)
    latest_post = posts.order_by('-date_added').first()

    context = {
        'total_posts': total_posts,
        'total_blogs': total_blogs,
        'total_views': total_views,
        'total_likes': total_likes,
        'latest_post': latest_post,
        'posts': posts.order_by('-date_added'),
    }

    return render(request, 'blogs/analytics.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    post.views += 1
    post.save()

    return render(request, 'blogs/post_detail.html', {'post': post})


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    post.likes += 1
    post.save()

    return redirect('blogs:post_detail', post_id=post.id)