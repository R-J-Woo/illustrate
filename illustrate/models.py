from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Illustrate(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=128, verbose_name='카테고리')
    description = models.TextField(verbose_name='작품 설명')
    price = models.IntegerField(verbose_name='작품 가격')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록 날짜')
    image = models.ImageField(verbose_name='일러스트')
