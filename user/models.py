from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models import Post


class User(AbstractUser):
    # phone = models.CharField('手机号码', max_length=11, unique=True)
    email = models.EmailField(unique=True)
    avatar = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='文章')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='父类目评论')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='被评论人')
    text = models.TextField('评论内容')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_time']
        db_table = 'comment'
