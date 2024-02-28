from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required

from django.views import generic
from .models import Post


class BlogHomeView(generic.ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'


class PostAdd(generic.CreateView):
    form_class = PostCreateForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('home')