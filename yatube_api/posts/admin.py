from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Регистрируем модель подписок в админке."""
    list_display = ('user', 'following',)
    search_fields = ('user__username', 'following__username')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Регистрируем модель групп в админке."""
    list_display = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Comment)
