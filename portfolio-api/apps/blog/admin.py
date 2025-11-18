from django.contrib import admin
from .models import Posts


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "slug", "created_at", "updated_at")
    list_filter = ("author", "created_at")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_at",)
