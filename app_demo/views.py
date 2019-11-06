from django.shortcuts import render

# Create your views here.
from app_demo.models import Student
import  random

def insert(request):
    for i in range(0,5):
        studentNum=int(random.uniform(0,1)*1000)
        student=Student()
        student.studentNum=studentNum
        student.name='大大超人'+str(i)+"号"
        student.age=15
        student.sex=random.choice([True,False])
        student.mobile=int(random.uniform(0,1)*1000)
        student.save()
        return