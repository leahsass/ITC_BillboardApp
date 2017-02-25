from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
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



# class UserFormView(View):
#     form_class = UserForm
#     # html file that form is included in
#     template_name = 'billboard_app/index.html' # new template?
#
#     # display blank form for new user
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     # process form database
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save(commit=False)
#
#             # get cleaned data (data that is formatted properly
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#             return redirect('index')