from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'content')
    raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
