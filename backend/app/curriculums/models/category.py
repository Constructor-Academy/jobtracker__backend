import uuid

from django.conf import settings
from django.db import models


class Category(models.Model):
    id = models.UUIDField(
        verbose_name='uuid',
        default=uuid.uuid4,
        primary_key=True
    )
    user = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='categories',
        to=settings.AUTH_USER_MODEL
    )
    name = models.CharField(
        max_length=50,
        blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'Category ID {self.id}: {self.name}'
