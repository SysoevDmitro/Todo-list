from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return f"{self.content}, {self.created}, {self.deadline}, {self.is_done}, {self.tags}"
