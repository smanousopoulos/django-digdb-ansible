from django.contrib.auth.models import User

User.objects.create_superuser('{{django.admin.user}}', '{{django.admin.email}}', '{{django.admin.pass}}')
