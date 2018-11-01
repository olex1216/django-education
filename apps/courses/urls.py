# encoding: utf-8

__author__ = 'hayden'
__date__ = '2018/11/1 16:35'

from .views import CourseListView

from django.urls import path

app_name = "courses"

urlpatterns = [
    # 课程列表url
    path('list/', CourseListView.as_view(), name="list"),

]
