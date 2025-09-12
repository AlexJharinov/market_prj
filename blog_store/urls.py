from django.urls import path
from blog_store.views import BlogListView, BlogDetailView, BlogEditView, BlogCreateView, BlogDeleteView

app_name = 'blog_store'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/edit/', BlogEditView.as_view(), name='blog_edit'),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),

]
