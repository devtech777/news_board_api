from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^api/posts$", views.posts_list),
    url(r"^api/posts/(?P<post_id>[0-9]+)$", views.post_detail),
    url(r"^api/posts/(?P<post_id>[0-9]+)/comments$", views.comments_list),
    url(r"^api/posts/(?P<post_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)$",
        views.comment_detail),
    url(r"^api/posts/(?P<post_id>[0-9]+)/upvote$", views.post_upvote),
]
