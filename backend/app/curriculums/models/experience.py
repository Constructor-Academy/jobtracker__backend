import uuid

from django.conf import settings
from django.db import models


class Experience(models.Model):
    id = models.UUIDField(
        verbose_name='uuid',
        default=uuid.uuid4,
        primary_key=True
    )
    user = models.ForeignKey(
        verbose_name='user',
        on_delete=models.CASCADE,
        related_name='experiences',
        to=settings.AUTH_USER_MODEL
    )
    job_title = models.CharField(
        verbose_name='job title',
        max_length=50,
        blank=True
    )
    employer = models.CharField(
        verbose_name='employer',
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
        verbose_name='job description',
        max_length=400,
        blank=True
    )
    webpage = models.URLField(
        verbose_name='employer web page',
        blank=True,
        null=True
    )
    contact = models.CharField(
        verbose_name='reference contact',
        max_length=200,
        blank=True
    )

    def __str__(self):
        return self.job_title
