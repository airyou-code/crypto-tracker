from django.utils.translation import gettext_lazy as _
from django.db import models
# from core.models import CoreModel
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from cryptotracker.models import Cryptocurrency
# Create your models here.


class AppUser(AbstractUser):
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


def set_uesr_permission(user):
    user_permissions: list = [
        Permission.objects.get(
            codename='view_cryptocurrency',
            content_type=ContentType.objects.get_for_model(Cryptocurrency)
        ),
        # Permission.objects.get(
        #     codename='view_cryptocurrency',
        #     content_type=ContentType.objects.get_for_model(Cryptocurrency)
        # ),
        # Permission.objects.get(
        #     codename='view_cryptocurrency',
        #     content_type=ContentType.objects.get_for_model(Cryptocurrency)
        # ),
    ]

    user.user_permissions.add(*user_permissions)
