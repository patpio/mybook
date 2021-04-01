from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from extra_views import CreateWithInlinesView

from posts.forms import PostImageInline
from posts.models import Post


class CreatePost(LoginRequiredMixin, CreateWithInlinesView):
    model = Post
    fields = ['title', 'slug', 'context']
    inlines = [PostImageInline]
    template_name = 'posts/create_post.html'
    login_url = reverse_lazy('account_login')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'context']
    template_name = 'posts/edit_post.html'
    login_url = reverse_lazy('account_login')
    success_url = reverse_lazy('home')


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    login_url = reverse_lazy('account_login')
    success_url = reverse_lazy('home')
