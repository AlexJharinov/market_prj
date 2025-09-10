from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView

from blog_store.models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = "blog_store/blog_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(publication_sign=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_store/blog_detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)  # получаем статью
        obj.number_views += 1  # увеличиваем счётчик
        obj.save(update_fields=["number_views"])  # сохраняем только поле views
        return obj

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'publication_sign']
    template_name = 'blog_store/blog_edit.html'

    def get_success_url(self):

        return reverse('blog_detail', kwargs={'pk': self.object.pk})

class BlogEditView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'publication_sign']
    template_name = 'blog_store/blog_edit.html'
    success_url = reverse_lazy('blog_store:blog_list')