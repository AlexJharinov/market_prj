from django.contrib import admin

from users.models import User



@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    """
        Админка в Django
    """
    list_display = ('id','email')

