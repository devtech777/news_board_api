from django.db import models
from django.utils import timezone


class Post(models.Model):
    # post title
    title = models.CharField(max_length=100, null=False)
    # post link
    link = models.CharField(max_length=255, null=False)
    # post creation date
    creation_date = models.DateTimeField(default=timezone.now)
    # amount of upvotes
    upvotes_amount = models.IntegerField(default=0)
    # author name
    author_name = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ["-creation_date"]

    # TODO Change these methods
    def upvote(self):
        self.upvotes_amount += 1
        self.save()

    def reset_upvotes(self):
        self.upvotes_amount = 0
        self.save()

    def __str__(self):
        return "{} - {}".format(self.title, self.link)


class Comment(models.Model):
    # many-to-one relationship with the Post model
    post_id = models.ForeignKey(
            Post,
            on_delete=models.CASCADE,
            related_name="comments"
        )
    # comment author name
    author_name = models.CharField(max_length=100, null=False)
    # comment content
    content = models.TextField()
    # creation date
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["creation_date"]

    def __str__(self):
        return "Comment {} by {}".format(self.content, self.author_name)
