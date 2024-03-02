from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from myApp.models import Student


# Create your views here.
def index(request):
    return render(request, "index.html")


def add(request):
    # 方式一
    # stu = Student(name="周欣雨2", age=20, birthday="2002-5-13", sex=1, classmate=1)
    # stu.save()

    # 方式二
    stu = Student.objects.create(name="周欣雨3", age=20, birthday="2002-5-13", sex=1, classmate=1)

    return HttpResponse("添加记录成功")


def select_student(request):
    stu = Student.objects.all()
    student_list = list(stu.values("name", "age"))

    import json
    a = json.dumps(student_list, ensure_ascii=False)

    return HttpResponse(a)

