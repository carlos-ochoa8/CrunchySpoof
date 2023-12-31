from django.db import models
from django.db.models import CASCADE
from users.models import User
from episodes.models import Episode


class EpisodeComment(models.Model):
    episode = models.ForeignKey(Episode, on_delete=CASCADE, null=False)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
