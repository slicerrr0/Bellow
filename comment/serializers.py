from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField()
    class Meta:
        model = Comment
        fields = ('id', 'community', 'author', 'parent', 'message')