from rest_framework import serializers

from .models import Post, Comment, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'created',)
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Group
