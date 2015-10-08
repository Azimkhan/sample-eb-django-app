import django
import os
from django.conf import settings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sample_app.settings.dev")
    django.setup()

    from django.contrib.auth.models import User
    
    admin_username = 'admin'
    admin_password = 'admin'

    admin = User.objects.filter(username=admin_username).first()

    if not admin:
        u = User(username=admin_username)
        u.set_password(admin_password)
        u.is_superuser = True
        u.is_staff = True
        u.save()