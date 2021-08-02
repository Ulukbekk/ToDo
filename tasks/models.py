from django.db import models


class CompletedTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(done=False)

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    objects = models.Manager()
    notcompleted = CompletedTaskManager()

    def __str__(self):
        return self.title


