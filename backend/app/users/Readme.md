# Custom user model
This custom user model uses the email as the unique identification field of the user.
Get familiar with the fields the model ships by looking at models.py.
This User model comes with a custom manager which adds custom methods on User.objects. 
With one of them you can create unvalidated users during registration.
#### Installation & Usage
1. Make sure your settings.py contains the following:
```
INSTALLED_APPS = [
     ...
    'app.users',
    ...
]

AUTH_USER_MODEL = 'users.User'
```
2. Migrate
3. Add 
```
path('backend/api/users/', include('app.users.urls')),
```
to your root urls.py to have access to all user endpoints.


