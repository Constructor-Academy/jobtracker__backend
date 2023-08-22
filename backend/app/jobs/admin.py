from app.jobs.models import Job, AdminInvite
from django.contrib import admin

admin.site.register(AdminInvite)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'user', 'status', 'created')
    ordering = ('id',)
    search_fields = ('user__email',)
