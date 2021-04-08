from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView

from extra_views import CreateWithInlinesView, UpdateWithInlinesView

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


class PostList(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    paginate_by = 6
    context_object_name = 'posts'


class UpdatePost(LoginRequiredMixin, UpdateWithInlinesView):
    model = Post
    fields = ['title', 'slug', 'context']
    inlines = [PostImageInline]
    template_name = 'posts/edit_post.html'
    login_url = reverse_lazy('account_login')
    success_url = reverse_lazy('home')


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    login_url = reverse_lazy('account_login')
    success_url = reverse_lazy('home')
