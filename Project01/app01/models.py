from django.db import models

# Create your models here.
class UserInfo(models.Model):
    #id列，自增  主键
    #创建用户名列，字符串类型，指定长度
    username=models.CharField(max_length=32)
    pwd=models.CharField(max_length=64)

    user_type_choices=(

        (1,'超级用户'),
        (2,'普通用户'),
        (3,'普普通通用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices,default=1)
    user_group=models.ForeignKey('UserGroup',to_field='uid',default=1,on_delete=models.CASCADE)
class UserGroup(models.Model):
    uid=models.AutoField(primary_key=True)
    caption=models.CharField(max_length=32)
    ctime=models.DateTimeField(auto_now_add=True,null=True)
    uptime=models.DateTimeField(auto_now=True,null=True)
