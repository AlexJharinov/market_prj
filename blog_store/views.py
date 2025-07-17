
from django.views.generic import DetailView

from blog_store.models import Blog


class BlogDetailView(DetailView):
    model = Blog
