<<<<<<< HEAD
# Generated by Django 4.1.1 on 2022-09-09 09:29
=======
# Generated by Django 4.1.1 on 2022-09-09 08:17
>>>>>>> e9ae3b523566da25597a16b68da2b86a584fd8e0

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nickname', models.CharField(max_length=128, verbose_name='닉네임')),
<<<<<<< HEAD
                ('image', models.ImageField(upload_to='profile/', verbose_name='프로필 이미지')),
                ('is_author', models.BooleanField(default=False, verbose_name='작가 여부')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')),
=======
                ('image', models.ImageField(default='default.png', upload_to='profile/', verbose_name='이미지')),
                ('is_author', models.BooleanField(default=False, verbose_name='작가 여부')),
>>>>>>> e9ae3b523566da25597a16b68da2b86a584fd8e0
            ],
        ),
    ]
