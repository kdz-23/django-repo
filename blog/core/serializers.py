from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # Nested User Info

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
