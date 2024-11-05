from django.contrib import messages  # Import messages for user feedback
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm, UserRegistrationForm
from .models import Post


def home(request):
    if request.user.is_authenticated:
        return redirect("posts_home")

    return render(request, "blog/home.html", {"user": request.user})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "blog/register.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Wylogowano pomyślnie.")
    return redirect("home")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})


@login_required
def posts_home(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "blog/posts_home.html", {"posts": posts})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Blog post created successfully.")
            return redirect("home")
    else:
        form = PostForm()

    return render(request, "blog/create_post.html", {"form": form})


@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        messages.error(request, "You are not authorized to edit this entry.")
        return redirect("home")

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        messages.success(request, "Blog entry updated successfully.")
        return redirect("home")

    return render(request, "blog/update_post.html", {"entry": post})
