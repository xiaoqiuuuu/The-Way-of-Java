from django.urls import path

from myApp.views import *

urlpatterns = [
    path('indexes/', indexes, name="indexes"),
    path('',index , name="index"),
    path('allUser/' , getAllUser , name="getAllUser"),
    path('profile/<int:uid>/',getUser , name="getUser"),
    path('testRequest/',testRequest , name="testRequest")
]