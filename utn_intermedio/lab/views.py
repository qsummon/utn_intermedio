from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Post
# from django.http import HttpResponse


def home(request):
    # return HttpResponse('<h1>lab Home</h1>')
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'lab/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'lab/home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'subtitle', 'content']
    fields = ['titulo', 'descripcion', 'contenido']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # fields = ['title', 'subtitle', 'content']
    fields = ['titulo', 'descripcion', 'contenido']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    # return HttpResponse('<h1>lab About</h1>')
    return render(request, 'lab/about.html', {'title': 'About'})
