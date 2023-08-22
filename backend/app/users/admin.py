from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    readonly_fields = ('date_joined',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin', 'is_booklet_author', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
        ('Administered Users', {'fields': ('administered_users',)}),
        ('Additional fields for CV', {'fields': ('street', 'zip', 'city', 'country', 'phone', 'date_of_birth',
                                                 'user_description', 'nationality', 'permit', 'linkedin_profile',
                                                 'github_profile', 'actual_position', 'final_project', 'job_search_area')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    ordering = ('email',)
