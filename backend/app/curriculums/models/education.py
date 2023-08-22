import uuid

from django.conf import settings
from django.db import models


class Education(models.Model):
    id = models.UUIDField(
        verbose_name='uuid',
        default=uuid.uuid4,
        primary_key=True
    )
    user = models.ForeignKey(
        verbose_name='user',
        on_delete=models.CASCADE,
        related_name='educations',
        to=settings.AUTH_USER_MODEL
    )
    education_title = models.CharField(
        verbose_name='education title',
        max_length=50,
        blank=True
    )
    institute = models.CharField(
        verbose_name='education institute',
        max_length=50,
        blank=True
    )
    city = models.CharField(
        verbose_name='city',
        max_length=50,
        blank=True
    )
    country = models.CharField(
        verbose_name='country',
        max_length=50,
        blank=True
    )
    start_date = models.DateField(
        verbose_name='start date',
        null=True
    )
    end_date = models.DateField(
        verbose_name='end date',
        null=True
    )
    description = models.CharField(
        verbose_name='education description',
        max_length=400,
        blank=True
    )
    webpage = models.URLField(
        verbose_name='education web page',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.education_title
