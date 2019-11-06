from django.db import models

# Create your models here.
class Student(models.Model):
    """
    创建如下几个表的字段
    """
    # 学号 primary_key=True: 该字段为主键
    studentNum = models.CharField('学号', primary_key=True, max_length=15)
    # 姓名 字符串 最大长度20
    name = models.CharField('姓名', max_length=20)
    # 年龄 整数 null=False, 表示该字段不能为空
    age = models.IntegerField('年龄', null=False)
    # 性别 布尔类型 默认True: 男生 False:女生
    sex = models.BooleanField('性别', default=True)
    # 手机 unique=True 该字段唯一
    mobile = models.CharField('手机', unique=True, max_length=15)
    # 创建时间 auto_now_add：只有在新增的时候才会生效
    createTime = models.DateTimeField(auto_now_add=True)
    # 修改时间 auto_now： 添加和修改都会改变时间
    modifyTime = models.DateTimeField(auto_now=True)

    # 指定表名 不指定默认APP名字——类名(app_demo_Student)
    class Meta:
        db_table = 'student'

