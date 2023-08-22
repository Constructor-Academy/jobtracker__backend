import uuid

from django.conf import settings
from django.db import models


class Skill(models.Model):
    id = models.UUIDField(
        verbose_name='uuid',
        default=uuid.uuid4,
        primary_key=True
    )
    user = models.ForeignKey(
        verbose_name='user',
        on_delete=models.CASCADE,
        related_name='skills',
        to=settings.AUTH_USER_MODEL,
        blank=True
    )
    tag = models.CharField(
        verbose_name='skill tag',
        max_length=32,
    )
    level = models.CharField(
        verbose_name='level',
        max_length=2,
        choices=(
            ('BA', 'Basic'),
            ('IM', 'Intermediate'),
            ('PR', 'Proficient'),
        ),
        default='PR'
    )

    def __str__(self):
        return self.tag
