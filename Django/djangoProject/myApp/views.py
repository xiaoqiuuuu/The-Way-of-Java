import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from myApp.models import UserModel


# Create your views here.
def index(request):
    return render(request, "index.html")


def indexes(request):
    return render(request, 'indexes.html')


def getAllUser(request):
    userList = UserModel.objects.all();
    print(userList)
    return render(request, 'allUser.html', {'userList': userList})


def getUser(request, uid):
    user = UserModel.objects.get(pk=uid)
    return render(request, 'userDetail.html', {'user': user})


def testRequest(request):
    a = {}
    a["lalal"] = "sfsfdsd"

    a["requestBody"] = str(request.body)
    a["requestHead"] = str(request.headers)

    return JsonResponse(a)
