import uuid

from django.conf import settings
from django.db import models


class Job(models.Model):
    id = models.UUIDField(
        verbose_name='uuid',
        default=uuid.uuid4,
        primary_key=True
    )
    index = models.IntegerField(
        verbose_name='index',
    )
    user = models.ForeignKey(
        verbose_name='user',
        on_delete=models.CASCADE,
        related_name='jobs',
        to=settings.AUTH_USER_MODEL
    )
    url = models.CharField(
        max_length=10000,
        verbose_name='url',
        blank=True
    )
    title = models.TextField(
        verbose_name='job title',
        blank=True
    )
    category = models.CharField(
        verbose_name='categories',
        choices=(
            ('Finance', 'Finance'),
            ('Information Technology', 'Information Technology'),
            ('Education and Training', 'Education'),
            ('Business Administration', 'Business'),
            ('Marketing and Sales', 'Marketing'),
            ('Health Science', 'Health'),
            ('Technology', 'Technology'),
            ('Others', 'Others')
        ),
        max_length=100,
        default='Others'
    )
    description = models.TextField(
        verbose_name='job description',
        blank=True
    )
    image = models.ImageField(
        verbose_name='scarepd image',
        upload_to='',
        blank=True,
        null=True
    )
    company = models.TextField(
        verbose_name='company',
        blank=True
    )
    company_street = models.CharField(
        verbose_name='company street',
        max_length=50,
        blank=True
    )
    company_zip = models.CharField(
        verbose_name='company zip',
        max_length=8,
        blank=True
    )
    company_city = models.CharField(
        verbose_name='company city',
        max_length=50,
        blank=True
    )
    company_country = models.CharField(
        verbose_name='company country',
        max_length=50,
        blank=True
    )
    contact = models.TextField(
        verbose_name='company contact',
        max_length=50,
        blank=True
    )
    contact_title = models.CharField(
        verbose_name='company contact title',
        max_length=50,
        blank=True
    )
    contact_phone = models.CharField(
        verbose_name='company contact phone',
        max_length=16,
        blank=True
    )
    contact_email = models.EmailField(
        verbose_name='company contact email',
        max_length=50,
        blank=True
    )
    notes = models.TextField(
        verbose_name='notes',
        blank=True
    )
    status = models.CharField(
        verbose_name='status',
        max_length=2,
        choices=(
            ('WH', 'Wishlist'),
            ('AP', 'Applied'),
            ('IN', 'Interviewing'),
            ('OF', 'Offered'),
            ('AC', 'Accepted'),
            ('RJ', 'Rejected'),
        ),
        default='WH'
    )
    cv = models.FileField(
        verbose_name='cv',
        upload_to='cvs/',
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        verbose_name='created',
        null=True
    )

    class Meta:
        unique_together = ('id', 'index', 'status', 'user')

    def save(self, **kwargs):
        if self.index is None:
            self.index = Job.objects.all().count()
        return super(Job, self).save(**kwargs)

    def __str__(self):
        return self.title or self.user.email
