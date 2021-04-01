from extra_views import InlineFormSetFactory

from posts.models import PostImage


class PostImageInline(InlineFormSetFactory):
    model = PostImage
    fields = ['image']
