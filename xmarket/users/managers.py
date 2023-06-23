from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, country_code, phone_number, email, password=None, name=None):
        if not email:
            raise ValueError("The Email field must be set")
        if not country_code or not phone_number:
            raise ValueError("Country code and phone number must be set")

        user = self.model(
            country_code=country_code,
            phone_number=phone_number,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.name = name
        user.save(using=self._db)

        # Remove the line below to avoid saving the user object twice

        return user

    def create_superuser(self, country_code, phone_number, email, password=None, name=None):
        user = self.create_user(
            country_code=country_code,
            phone_number=phone_number,
            email=email,
            password=password,
            name=name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
