# from django.contrib import admin
from django.urls import path, include
from account.views import EducationInfoView, ExperienceInfoView, PersonalInfoView, SkillInfoView, UpdateEducationInfoView, UpdateExperienceInfoView,UpdatePersonalInfoView, UserPasswordResetView, UserRegistrationView,UserLoginView, UserProfileView, UserChangePasswordView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    # path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset_password'),
    path('personalinfo/', PersonalInfoView.as_view(), name='personal-info'),
    path('updatepersonalinfo/<int:pk>/', UpdatePersonalInfoView.as_view(), name='update-personal-info'),
    path('educationinfo/', EducationInfoView.as_view(), name='education-info'),
    path('updateeducationinfo/<int:pk>/', UpdateEducationInfoView.as_view(), name='update-education-info'),
    path('experienceinfo/', ExperienceInfoView.as_view(), name='experience-info'),
    path('updateexperienceinfo/<int:pk>/', UpdateExperienceInfoView.as_view(), name='update-experience-info'),
    path('skillsinfo/', SkillInfoView.as_view(), name='skills-info'),
    
    
    
]
