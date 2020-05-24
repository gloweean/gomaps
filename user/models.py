from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            username=username,
            email=MyUserManager.normalize_email(email),
            name=name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, name, password):
        u = self.create_user(username=username,
                             email=email,
                             name=name,
                             password=password,
                             )
        u.is_admin = True
        u.is_staff = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICE = (
        ('MALE', '남자'),
        ('FEMALE', '여자'),
        ('OTHER', '기타'),
    )
    username = models.CharField(unique=True, max_length=100, blank=True, null=True, verbose_name='ID')
    store_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='사업장 이름')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='사용자명')
    email = models.EmailField(unique=True, blank=False, null=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default='OTHER', )
    birthday = models.DateField(blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )

    date_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    object = MyUserManager()