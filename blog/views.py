from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DeleteView
from django.views.generic.edit import CreateView # forms
from .models import Post

class BlogListView(ListView):
    model=Post
    template_name='home.html'

class BlogDetailView(DeleteView):
    model=Post
    template_name='post_detail.html'

class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title','author','body']