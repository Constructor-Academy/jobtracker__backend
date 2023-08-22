from django.db import models
from app.emails.models import Email


class AdminInvite(models.Model):
    user_email = models.EmailField(
        verbose_name='user'
    )
    admin_email = models.EmailField(
        verbose_name='admin email'
    )
    status = models.CharField(
        verbose_name='status',
        max_length=2,
        choices=(
            ('1', 'Admin invited to open account'),
            ('2', 'Admin existed and has been added as admin of requesting user.'),
            ('3', 'Admin account created and added as admin of requesting user.')
        )
    )
    email = models.ForeignKey(
        verbose_name='sent email invite',
        to=Email,
        related_name='invites',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user_email}->{self.admin_email}'
