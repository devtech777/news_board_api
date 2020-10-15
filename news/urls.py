from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r"^api/posts$",
        views.PostViewSet.as_view(
            {"get": "list", "post": "create", "delete": "destroy"}
        ),
    ),
    url(
        r"^api/posts/(?P<pk>[0-9]+)$",
        views.PostViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    url(
        r"^api/posts/(?P<pk>[0-9]+)/upvote$",
        views.PostViewSet.as_view({"patch": "partial_update"}),
    ),
    url(
        r"^api/posts/(?P<pk>[0-9]+)/comments$",
        views.CommentViewSet.as_view(
            {"get": "list", "post": "create", "delete": "destroy"}
        ),
    ),
    url(
        r"^api/posts/(?P<pk>[0-9]+)/comments/(?P<comment_id>[0-9]+)$",
        views.CommentViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]
