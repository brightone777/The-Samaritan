from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'user', 'ip_address', 'blocked')
    list_filter = ('blocked', 'created_at')
    search_fields = ('content', 'ip_address', 'user__username')
    actions = ['mark_as_blocked', 'mark_as_unblocked']

    @admin.action(description="Block selected posts")
    def mark_as_blocked(self, queryset):
        queryset.update(blocked=True)

    @admin.action(description="Unblock selected posts")
    def mark_as_unblocked(self, queryset):
        queryset.update(blocked=False)
