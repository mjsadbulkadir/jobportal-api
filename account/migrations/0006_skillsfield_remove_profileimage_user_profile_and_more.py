# Generated by Django 4.2.7 on 2023-12-07 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_userprofile_profileimage_backgroundimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skillsfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='profileimage',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='skillsinfo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='skillsinfo',
            name='name',
        ),
        migrations.AlterField(
            model_name='skillsinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='BackgroundImage',
        ),
        migrations.DeleteModel(
            name='ProfileImage',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='skillsinfo',
            name='skill_field',
            field=models.ManyToManyField(to='account.skillsfield'),
        ),
    ]
