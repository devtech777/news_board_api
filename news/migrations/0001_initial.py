# Generated by Django 3.1.2 on 2020-10-13 12:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("link", models.CharField(max_length=255)),
                (
                    "creation_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("upvotes_amount", models.IntegerField(default=0)),
                ("author_name", models.CharField(max_length=100)),
            ],
            options={
                "ordering": ["-creation_date"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author_name", models.CharField(max_length=100)),
                ("content", models.TextField()),
                (
                    "creation_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="news.post",
                    ),
                ),
            ],
            options={
                "ordering": ["creation_date"],
            },
        ),
    ]
