from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Manager for the User model.
    """
    def create_user(self, email, password, is_admin=False, is_active=False):
        """
        Creates a new user instance.
        Never use User.objects.create() to create users which sets the password in plain-text.
        Instead use User.objects.create_user() which will properly hash and set the password.
        """
        email = self.normalize_email(email)
        if self.model.objects.filter(email=email, is_active=False):
            user = self.model.objects.get(email=email)
        else:
            user = self.model(email=email)
        user.is_admin = is_admin
        user.is_active = is_active
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Creates a new superuser having admin privileges.
        This method is called when creating a superuser using 'python manage.py createsuperuser'.
        """
        user = self.create_user(
            email=email,
            password=password,
            is_admin=True,
            is_active=True
        )
        return user
