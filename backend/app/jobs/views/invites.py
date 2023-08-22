from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app.emails.signals import send_email
from app.jobs.models import AdminInvite
from app.jobs.serializers import AdminInviteSerializer

User = get_user_model()


class CreateInvite(GenericAPIView):
    serializer_class = AdminInviteSerializer

    def post(self, request, *args, **kwargs):
        serialzer = self.get_serializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        user = request.user
        # check if account for admin already exists
        try:
            admin = User.objects.get(email=serialzer.data['admin_email'])
        except User.DoesNotExist:
            # Send invite to admin email to create account
            # email = Email(
            #     to=serialzer.data['admin_email'],
            #     subject='You have been invited to Job Tracker',
            #     content=f'{user.email} has invited you to his job board but you need an account first. Please register.'
            # )
            # email.save(request=request)
            send_email.send(sender=User, request=request, to=serialzer.data['admin_email'], email_type='admin_invite', email=user.email)

            admin_invite = AdminInvite(
                user_email=user.email,
                admin_email=serialzer.data['admin_email'],
                status='1'
            )
            admin_invite.save()
            return Response(status=200)
        if not admin.is_admin:
            return Response({'admin_email': 'User is not an admin'}, status=400)
        if admin.is_admin and user in admin.administered_users.all():
            return Response({'admin_email': 'You have already invited this admin.'}, status=400)
        admin.administered_users.add(user)
        # email = Email(
        #     to=serialzer.data['admin_email'],
        #     subject='You have been invited to Job Tracker',
        #     content=f'{user.email} has invited you to his/her job board! You can now access his/her job board in your admin section.'
        # )
        # email.save(request=request)
        send_email.send(sender=User, request=request, to=serialzer.data['admin_email'], email_type='admin_invite', email=user.email)

        admin_invite = AdminInvite(
            user_email=user.email,
            admin_email=serialzer.data['admin_email'],
            status='2'
        )
        admin_invite.save()
        return Response(status=200)


@receiver(post_save, sender=User)
def add_rel_if_pending(sender, instance, **kwargs):
    # Get invites that are pending because admin din't exist
    admin = instance
    invites = AdminInvite.objects.filter(admin_email=admin.email, status='1')
    if len(invites) > 0 and not admin.is_admin:
        admin.is_admin = True
        admin.save()
    for invite in invites:
        try:
            user = User.objects.get(email=invite.user_email)
        except User.DoesNotExist:
            continue
        admin.administered_users.add(user)
        invite.status = '3'
        invite.save()
