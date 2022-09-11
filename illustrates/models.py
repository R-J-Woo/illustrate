from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.


class Illustrates(models.Model):
    illustrator = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='작가', related_name='author_illustrates')
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name='작가 프로필')
    image = models.ImageField(verbose_name='일러스트')
    title = models.CharField(max_length=128, verbose_name='작품명')
    category = models.CharField(max_length=128, verbose_name='카테고리')
    description = models.TextField(verbose_name='작품 설명')
    purchase_number = models.IntegerField(verbose_name='구매수')
    likes = models.ManyToManyField(
        User, related_name='like_illustrates', blank=True, verbose_name='좋아요')
    price = models.IntegerField(verbose_name='작품 가격')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록 날짜')


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    illustrate = models.ForeignKey(
        Illustrates, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
