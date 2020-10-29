from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post, Comment, Group, Follow

User = get_user_model


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        exclude = ('group',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('description',)
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    following = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        exclude = ('id',)
        model = Follow
