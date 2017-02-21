from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'billboard_app/index.html', {'post_list': posts})



def new_post(request):
    title = request.POST.get('title')
    text = request.POST.get('user-input')
    author = request.POST.get('author')

    new_post = Post(title, text, author, date=timezone.now())
    new_post.save()

    return HttpResponseRedirect ('billboard_app/index.html')



# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('index', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'billboard_app/index.html', {'form': form})