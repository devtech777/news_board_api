from news.models import Post


def reset_votes():
    posts = Post.objects.all()
    for post in posts:
        post.upvotes_amount = 0
        post.save()
