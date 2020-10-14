from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'author_name',
            'content',
            'creation_date',
            'post_id'
        )


class PostSerializer(serializers.ModelSerializer):
    # post comments
    comments = CommentSerializer(required=False, many=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "upvotes_amount",
            "author_name",
            "comments"
        )
