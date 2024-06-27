import os

from django.core.management import BaseCommand

from apps.users.models import User

email_admin = os.getenv('EMAIL_ADMIN')
name_admin = os.getenv('NAME_ADMIN')
password = os.getenv('PASSWORD')


class Command(BaseCommand):
    """Добавление администратора. Вход и регистрация через e-mail почту is_staff=True, is_superuser=True"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email=email_admin,
            first_name=email_admin,
            last_name=name_admin,
            is_staff=True,
            is_superuser=True
        )

        user.set_password(password)
        user.save()
