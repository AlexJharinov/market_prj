from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from blog_store.models import Blog

class BlogListView(ListView):
    """
        Отображает список всех записей
    """
    model = Blog
    template_name = "blog_store/blog_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        """
            Метод для отображения статуса публикации.
        """
        return Blog.objects.filter(publication_sign=True)


class BlogDetailView(DetailView):
    """
        Класс отображает подробное описание одного объекта.
    """
    model = Blog
    template_name = "blog_store/blog_detail.html"

    def get_object(self, queryset=None):
        """
            Метод для подсчета просмотров публикации.
        """
        obj = super().get_object(queryset)
        obj.number_views += 1
        obj.save(update_fields=["number_views"])
        return obj


class BlogEditView(UpdateView):
    """
        Класс для редактирования блога.
    """
    model = Blog
    fields = ['title', 'content', 'publication_sign']
    template_name = 'blog_store/blog_edit.html'
    success_url = reverse_lazy('blog_store:blog_list')


class BlogCreateView(CreateView):
    """
        Класс для создания блога
    """
    model = Blog
    fields = ("title", "content", "preview", "publication_sign")
    template_name = "blog_store/blog_create.html"
    success_url = reverse_lazy('blog_store:blog_list')


class BlogDeleteView(DeleteView):
    """
        Класс для удаления блога.
    """
    model = Blog
    template_name = "blog_store/product_delete.html"
    success_url = reverse_lazy("blog_store:blog_list")
