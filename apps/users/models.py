from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    """
    A custom manager for the User model instead of Django UserManager.
    """
    def create_user(self, email, date_of_birth, first_name=None, last_name=None,
                    language=1, company=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        if not date_of_birth:
            raise ValueError("Users must have a date of birth")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
            language=language,
            company=company,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """

        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            first_name=None,
            last_name=None,
            language=1,
            company=None,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    The User class is a custom implementation of the Django AbstractBaseUser model.
    It represents a user in the system and provides functionalities for user authentication and authorization.
    """
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    first_name = models.CharField(verbose_name="first name", max_length=32, blank=True, null=True)
    last_name = models.CharField(verbose_name="last name", max_length=32, blank=True, null=True)

    PYTHON = 1
    JAVASCRIPT = 2
    RUST = 3
    GOLANG = 4
    PHP = 5
    JAVA = 6

    LANGUAGE_FIELDS = (
        (PYTHON, 'Python'),
        (JAVASCRIPT, 'JavaScript'),
        (RUST, 'Rust'),
        (GOLANG, 'Go'),
        (PHP, 'php'),
        (JAVA, 'Java'),
    )
    language = models.PositiveSmallIntegerField(default=PYTHON, choices=LANGUAGE_FIELDS)

    company = models.CharField(max_length=32, blank=True, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Does the user have a specific permission?
        """
        return True

    def has_module_perms(self, app_label):
        """
        Does the user have permissions to view the app `app_label`?
        """
        return True

    @property
    def is_staff(self):
        """
        Is the user a member of staff?
        """
        return self.is_admin
