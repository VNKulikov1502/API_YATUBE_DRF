from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from posts.models import Post, Comment, Follow, Group
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)
from rest_framework.pagination import LimitOffsetPagination
from .permissions import AuthorOrReadOnly
from rest_framework.response import Response
from rest_framework import filters


def get_post_id(var):
    """Получаем ID поста."""
    return var.kwargs['post_id']


class FollowViewSet(viewsets.ModelViewSet):
    """Запросы подписок."""
    serializer_class = FollowSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        AuthorOrReadOnly,
    )
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.select_related(
            'user',
            'following'
        ).filter(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Запросы к комментариям поста."""
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Comment.objects.filter(post_id=get_post_id(self))

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=get_post_id(self))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ModelViewSet):
    """Запросы к группам."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {
                    'detail':
                    'Создание объектов доступно только администратору.'
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        return super().create(request, *args, **kwargs)


class PostViewSet(viewsets.ModelViewSet):
    """Запросы к постам."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
