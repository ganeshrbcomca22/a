from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Blog, Comment
from .forms import BlogForm, CommentForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blogging/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blogging/login.html', {'form': form})

@login_required
def create_blog_view(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blogging/create_blog.html', {'form': form})

@login_required
def add_comment_view(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.commenter = request.user
            comment.save()
            return redirect('view_blog', blog_id=blog_id)
    else:
        form = CommentForm()
    return render(request, 'blogging/add_comment.html', {'form': form})

def view_blog_view(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    comments = Comment.objects.filter(blog=blog)
    return render(request, 'blogging/view_blog.html', {'blog': blog, 'comments': comments})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blogging/home.html', {'blogs': blogs})
