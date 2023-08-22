from django.conf import settings
from django.db import models


class Feedback(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        on_delete=models.CASCADE,
        related_name='user_feedback',
        to=settings.AUTH_USER_MODEL
    )
    title = models.CharField(
        verbose_name='feedback title',
        max_length=100,
        blank=True
    )
    content = models.TextField(
        verbose_name='feedback content',
        max_length=300,
        default=False
    )
    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.user.email} - {self.title}'
