from django.urls import path

from myApp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('select/', select_student, name='selectStudent'),

]