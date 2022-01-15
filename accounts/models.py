from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from accounts.manager import UserManager


class User(AbstractBaseUser):
    class Status(models.TextChoices):
        PLACED = 'pl', 'Placed'
        UNPLACED = 'up', 'Unplaced'

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.UNPLACED)
    aggregate = models.PositiveSmallIntegerField(blank=True, null=True)
    department = models.ForeignKey('departments.Department', blank=True, null=True,
                                   on_delete=models.CASCADE, related_name='students')

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        get_latest_by = 'created_at'

    def __str__(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.is_admin
    
    def has_perm(self, perm, obj=None):
        """
        Does the user have a specific permission?
        Simplest possible answer: Yes, always
        """
        return True

    def has_module_perms(self, app_label):
        """
        Does the user have permissions to view the app `app_label`?
        Simplest possible answer: Yes, always
        """
        return True
