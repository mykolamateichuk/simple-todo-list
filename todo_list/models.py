from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")
