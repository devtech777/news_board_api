from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from news.models import Post, Comment
from news.serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view


@api_view(["GET", "POST", "DELETE"])
def posts_list(request):
    # GET list of posts, POST a new post, DELETE all posts
    if request.method == "GET":
        posts = Post.objects.all()
        if len(posts) == 0:
            return JsonResponse(
                {"message": "There are no posts"}, status=status.HTTP_404_NOT_FOUND
            )
        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)
    elif request.method == "POST":
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        count = Post.objects.all().delete()[0]
        return JsonResponse(
            {"message": "{} posts were deleted successfully!".format(count)},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, post_id):
    # find post by pk (post_id)
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse(
            {"message": "The post does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    # GET / PUT / DELETE post
    if request.method == "GET":
        post_serializer = PostSerializer(post)
        return JsonResponse(post_serializer.data)
    elif request.method == "PUT":
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(post, data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data)

        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        post.delete()
        return JsonResponse(
            {"message": "Post was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["PATCH"])
def post_upvote(request, post_id):
    # find post by pk (post_id)
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse(
            {"message": "The post does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "PATCH":
        upvotes_amount = post.upvotes_amount + 1
        post_serializer = PostSerializer(
            post, data={"upvotes_amount": upvotes_amount}, partial=True
        )
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data)

        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST", "DELETE"])
def comments_list(request, post_id):
    # find post by pk (post_id)
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse(
            {"message": "The post does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    # GET list of comments, POST a new comment, DELETE all comments
    if request.method == "GET":
        comments = post.comments.all()
        if len(comments) == 0:
            return JsonResponse(
                {"message": "There are no comments for post ID = {}".format(post_id)},
                status=status.HTTP_404_NOT_FOUND,
            )
        comments_serializer = CommentSerializer(comments, many=True)
        return JsonResponse(comments_serializer.data, safe=False)
    elif request.method == "POST":
        post_data = JSONParser().parse(request)
        post_data["post_id"] = post_id
        comment_serializer = CommentSerializer(data=post_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == "DELETE":
        count = post.comments.all().delete()[0]
        return JsonResponse(
            {"message": "{} comments were deleted successfully!".format(count)},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "PUT", "DELETE"])
def comment_detail(request, post_id, comment_id):
    # find comment by pk(comment_id)
    try:
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        return JsonResponse(
            {"message": "The comment does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    # GET / PUT / DELETE post
    if request.method == "GET":
        comment_serializer = CommentSerializer(comment)
        return JsonResponse(comment_serializer.data)
    elif request.method == "PUT":
        post_data = JSONParser().parse(request)
        post_data["post_id"] = post_id
        comment_serializer = CommentSerializer(comment, data=post_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data)

        return JsonResponse(
            comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == "DELETE":
        comment.delete()
        return JsonResponse(
            {"message": "Comment was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )
