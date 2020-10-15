from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from news.models import Post, Comment
from news.serializers import PostSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def partial_update(self, request, pk):
        post = Post.objects.get(pk=pk)
        upvotes_amount = post.upvotes_amount + 1
        post_serializer = PostSerializer(
            post, data={"upvotes_amount": upvotes_amount}, partial=True
        )
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data)

        return JsonResponse(
            post_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class CommentViewSet(ModelViewSet):
    def list(self, request, pk=None):
        queryset = Comment.objects.filter(post_id=pk)
        comments_serializer = CommentSerializer(queryset, many=True)
        return JsonResponse(comments_serializer.data, safe=False)

    def create(self, request, pk=None):
        post_data = JSONParser().parse(request)
        post_data["post_id"] = pk
        comment_serializer = CommentSerializer(data=post_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data)

        return JsonResponse(
            comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None, comment_id=None):
        comment = Comment.objects.get(pk=comment_id)
        comment_serializer = CommentSerializer(comment)
        return JsonResponse(comment_serializer.data)

    def update(self, request, pk=None, comment_id=None):
        post_data = JSONParser().parse(request)
        post_data['post_id'] = pk
        comment = Comment.objects.get(pk=comment_id)
        comment_serializer = CommentSerializer(comment, data=post_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data)

        return JsonResponse(
            comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None, comment_id=None):
        if comment_id:
            comment = Comment.objects.get(pk=comment_id)
            comment.delete()
        else:
            post = Post.objects.get(pk=pk)
            post.comments.all().delete()

        return JsonResponse(
            {"message": "Comment(s) were deleted successfully!"}
        )
