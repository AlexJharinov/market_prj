from django.contrib import admin

from blog_store.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
        Админка для главной панели в Django.
    """
    list_display = ('title','creation_at', 'publication_sign', 'number_views')
    list_filter = ('creation_at', 'publication_sign')
    search_fields = ('title', 'content')

