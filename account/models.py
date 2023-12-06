from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# custom user manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email, name,tc 
         and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None, ):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# custom user model

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.CharField(max_length=50)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    contact =models.CharField(max_length=10)
    dob = models.DateField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.fname

class EducationInfo(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    # user = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    board = models.CharField(max_length=20)
    passing_year = models.DateField()
    total_marks = models.IntegerField()
    percentage_cgpa= models.FloatField()
    
    def __str__(self):
        return self.education
    
class ExperienceInfo(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    year_of_experience = models.CharField(max_length=50)
    joining_date = models.DateField()
    resigning_date = models.DateField()
    job_role = models.CharField(max_length=100)
    
class SkillsInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='Default Name')  # Add default value here
    description = models.CharField(max_length=100, default='Default Description')

    def __str__(self):
        return self.name
    
    # upload image by using signals
    
# models.py

# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings
# from django.db import models

# class UserProfile(models.Model):
#   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # Other fields in your UserProfile model, if any

# class ProfileImage(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='profile_images')
    
#     @receiver(post_save, sender=UserProfile)
#     def create_profile_image(sender, instance, created, **kwargs):
#      if created:
#         ProfileImage.objects.create(user_profile=instance, image='Pictures\Camera Roll\stoneComputer.png')  
#         # Replace 'default_profile_image.jpg' with your default profile image path

# class BackgroundImage(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='background_images')
    
    
#     @receiver(post_save, sender=UserProfile)
#     def create_background_image(sender, instance, created, **kwargs):
#      if created:
#         BackgroundImage.objects.create(user_profile=instance, image="Pictures\Camera Roll\stoneComputer.png")  
#         # Replace 'default_background_image.jpg' with your default background image path

# from django.db.models.signals import post_save
# from django.dispatch import receiver


    
