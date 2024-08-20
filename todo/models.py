from __future__ import annotations

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self: Tag) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(
        null=True,
        blank=True,
    )
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    def __str__(self: Task) -> str:
        return self.content
