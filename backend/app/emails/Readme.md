# Email
This django app provides all the functionality needed for email sending. It has a DevEmails model in which one can whitelist emails so that one can thest email sending in development.
It also has an EmailType model to define email types that have to be sent. This model is a duplicate of the NotificationType model in app.notifications. It is separate to highlight the conceptual difference
between the admin group-notifications system and simple one off email sending to users.
#### API
1. This module exposes a Signal `send_email`.
To listen to this signal do:
```
send_email.send(sender=User, request=self.context['request'], to=email, email_type='registration_email', code=reg_profile.code)

def send_email(sender, request, to, email_type, code, **kwargs):
def handle_signal(sender, user, **kwargs):
    pass
```
This signal is used to send individual emails to users via celery.

#### Prerequisites
None
#### Installation & Usage
1. Install and add to your requirements.yml file: 
```
pip install django-extensions
pip install django-fullurl
```
2. Install the app
```
INSTALLED_APPS = [
     ...
    'fullurl',
     ...
    'app.emails',
]
```
3.Make sure you have:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
4.Add Email settings:
```
BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '***'
EMAIL_HOST_PASSWORD = '***'
DEFAULT_FROM_EMAIL = '***'
```
5. Add the following to the root urls.py file.
```
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```
6.Change the image sent with the email in the static folder.
7.Start a docker container with your full project in it running `python manage.py send_mail`.
```
version: '3'
services:
  email:
    image: "your_image"
    restart: always
    env_file:
      - ./database.env
    command: 'python manage.py send_mail'
    volumes:
      - ./backend:/backend
      - ./media-files:/media-files
      - ./static-files:/static-files
    depends_on:
      - database
      - api
```
8. Migrate
9. Save emails to the Email model and start up a container running this module with `python manage.py send_mail`.


