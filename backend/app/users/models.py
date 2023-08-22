from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)
    username = models.CharField(
        verbose_name='username',
        max_length=200,
        unique=True,
        blank=True
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=200,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=200,
        blank=True
    )
    street = models.CharField(
        verbose_name='street',
        max_length=200,
        blank=True,
    )
    zip = models.CharField(
        verbose_name='zip',
        max_length=8,
        blank=True,
    )
    city = models.CharField(
        verbose_name='city',
        max_length=200,
        blank=True,
    )
    country = models.CharField(
        verbose_name='country',
        max_length=200,
        blank=True,
    )
    phone = models.CharField(
        verbose_name='phone',
        max_length=16,
        blank=True,
    )
    date_of_birth = models.DateField(
        verbose_name='date of birth',
        blank=True,
        null=True,
    )
    user_description = models.CharField(
        verbose_name='user description',
        max_length=200,
        blank=True,
    )
    nationality = models.CharField(
        verbose_name='nationality',
        max_length=32,
        blank=True,
    )
    permit = models.CharField(
        verbose_name='permit',
        max_length=32,
        blank=True,
    )
    linkedin_profile = models.URLField(
        verbose_name='linkedin profile',
        blank=True,
    )
    github_profile = models.URLField(
        verbose_name='github profile',
        blank=True,
    )
    actual_position = models.CharField(
        verbose_name='actual_position',
        max_length=50,
        blank=True,
    )
    is_staff = models.BooleanField(
        verbose_name='staff status',
        default=False,
        help_text='Designates whether the user can log into this site.',
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True,
        help_text='Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.'
    )
    date_joined = models.DateTimeField(
        verbose_name='date joined',
        auto_now_add=True
    )
    is_admin = models.BooleanField(
        verbose_name='is admin',
        default=False,
        help_text="Permission needed to administrate other users in Jobtracker",
    )
    administered_users = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='admins',
        blank=True
    )
    avatar = models.ImageField(
        verbose_name='avatar',
        upload_to='',
        blank=True
    )
    final_project = models.CharField(
        max_length=80,
        blank=True
    )
    is_booklet_author = models.BooleanField(
        verbose_name='is booklet author',
        default=False,
        help_text="Permission needed to generate student booklets"
    )
    job_search_area = models.CharField(
        verbose_name="job search area",
        max_length=50,
        default="Flexible"
    )

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email  # avatar = models.ImageField(
