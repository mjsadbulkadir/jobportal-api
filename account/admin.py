from django.contrib import admin
from account.models import EducationInfo, ExperienceInfo, Profile, SkillsInfo, User, PersonalInfo,Skillsfield
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["id","email", "name", "tc","is_admin",]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name","tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)


@admin.register(PersonalInfo)
class PersonalAdmin(admin.ModelAdmin):
    list_display=['id','user','fname','lname','gender','contact','dob','address',]
    
@admin.register(EducationInfo)
class EducationAdmin(admin.ModelAdmin):
    list_display=['user','education','board','passing_year','total_marks','percentage_cgpa']
    
@admin.register(ExperienceInfo)
class ExperienceAdmin(admin.ModelAdmin):
    list_display=['user','company_name','year_of_experience','joining_date','resigning_date','job_role']
    
@admin.register(Skillsfield)
class SkillsAdmin(admin.ModelAdmin):
    list_display=['id','skills']
    
@admin.register(SkillsInfo)
class SkillsInfoAdmin(admin.ModelAdmin):
    list_display=['id','user','Skill']
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','image']
