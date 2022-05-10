from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, password=None, **extra_field):
        if not phone_number:
            raise ValueError("Phone no is Required")

        user = self.model(phone_number=phone_number, **extra_field)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_active', True)
        return self.create_user(phone_number, password, **extra_field)

    # def create_superuser(self,phone_number, password, **extra_fields):
    #     user = self.create_user(phone_number, password, is_staff=True, **extra_fields)
    #     user.is_active = True
    #     user.save(using=self._db)
    #     return self.create_user(phone_number,password,**extra_fields)