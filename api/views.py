from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework import viewsets

from .models import Post, Comment, Group
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, CommentSerializer, GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group',] 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,
                          IsAuthorOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Comment.objects.filter(post=self.kwargs['post_id'])
        return queryset


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

    # def get_queryset(self):
    #     queryset = Comment.objects.filter(post=self.kwargs['post_id'])
    #     return queryset