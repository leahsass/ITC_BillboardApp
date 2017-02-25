from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm, UserForm
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    form = PostForm()

    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'billboard_app/index.html', {'post_list': posts, 'form':form})



@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'billboard_app/index.html', {'form': form})



def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
    else:
        new_form = UserForm()
    return render(request, 'billboard_app/login.html', {'new_form': form})



def user_login(request):
