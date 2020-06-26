from django.views import generic
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, Blog
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User, auth
from django.contrib import messages


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save();
                print("User Created")
                return redirect(request, 'login')
        else:
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'blog/register.html')


def postview(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = PostForm()
    return render(request, 'blog/post.html', {'form': form})


def edit(request, pk, template_name='blog/edit.html'):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='blog/confirm_delete.html'):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object': post})
def data(request, template_name='blog/index.html' ):
    data = BlogForm.objects.all()
    print(data)
    return render(request, template_name, {'data': data})