from django.db import models


class Contact(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=100,
        blank=True
    )
    email = models.CharField(
        verbose_name='email',
        max_length=300,
        blank=True
    )
    comments = models.TextField(
        verbose_name='comments',
        max_length=500,
        blank=True
    )
    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.name} - {self.comments}'
