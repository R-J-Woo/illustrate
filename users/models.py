from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    # primary key를 User의 pk로 설정하여 통합적으로 관리
    nickname = models.CharField(max_length=128, verbose_name='닉네임')
    image = models.ImageField(upload_to='profile/', verbose_name='프로필 이미지')
    is_author = models.BooleanField(default=False, verbose_name='작가 여부')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록 날짜')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
