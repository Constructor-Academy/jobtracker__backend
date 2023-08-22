import uuid

from django.db import models
from app.curriculums.models.category import Category


class Event(models.Model):
    id = models.UUIDField(
        verbose_name='uuid',
        default=uuid.uuid4,
        primary_key=True
    )
    category = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='events',
        to=Category
    )
    title = models.CharField(
        max_length=50,
        blank=True
    )
    institution = models.CharField(
        max_length=50,
        blank=True
    )
    city = models.CharField(
        max_length=50,
        blank=True
    )
    country = models.CharField(
        max_length=50,
        blank=True
    )
    start_date = models.DateField(
        null=True,
        blank=True,
    )
    end_date = models.DateField(
        null=True,
        blank=True,
    )
    description = models.CharField(
        max_length=400,
        blank=True
    )
    link = models.URLField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('-end_date',)

    def __str__(self):
        return f'Event ID {self.id} from {self.category.user.email}: {self.title}'
