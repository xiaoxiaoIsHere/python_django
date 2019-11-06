from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app_demo.models import Student
import random

def insert(request):
    for i in range(0, 5):
        studentNum=int(random.uniform(0, 1)*1000)
        student = Student()
        student.studentNum = studentNum
        student.name='大大超人'+str(i)+"号"
        student.age=15
        student.sex=random.choice([True, False])
        student.mobile=int(random.uniform(0, 1)*1000)
        student.save()
    return HttpResponse('数据插入完毕')
def find(request):
    #sql = 'select * from student'
    # django 也可以执行原生的sql语句
    #result = Student.objects.raw(sql)

    # 查询name = tom1的数据
    result = Student.objects.filter(name='大大超人4号')
    """
    result为<class 'django.db.models.query.QuerySet'>的对象
    需要进行数据处理
    """
    arr = []
    for i in result:
        content = {'学号': i.studentNum, '姓名': i.name, '性别': i.sex}
        arr.append(content)
    print(arr)
    print(type(arr))
    return HttpResponse(arr)
def modify(request, studentNum):
    # 通过学号获取student对象
    student = Student.objects.get(studentNum=studentNum)
    # 设置student的name为jack
    student.name = 'jack'
    student.save()
    return HttpResponse('修改成功.')
def delete(request, studentNum):
    student = Student.objects.get(studentNum=studentNum)
    student.delete()
    return HttpResponse('删除成功.')
def insert(request):
    # 随机整数 作为学号
    for i in range(5, 10):
        studentNum = int(random.uniform(0, 1) * 10000000000)
        # 从models文件中获取student对象
        student = Student()
        # 给对象赋值
        student.studentNum = studentNum
        student.name = 'tom' + str(i)
        student.age = 15
        student.sex = random.choice([True, False])
        student.mobile = int(random.uniform(0, 1) * 10000000000)
        # 插入数据
        student.save()

    return HttpResponse('数据插入完毕')