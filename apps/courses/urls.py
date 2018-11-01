# encoding: utf-8

__author__ = 'hayden'
__date__ = '2018/11/1 16:35'

from .views import CourseListView,CourseDetailView

from django.urls import path,re_path

app_name = "courses"

urlpatterns = [
    # 课程列表url
    path('list/', CourseListView.as_view(), name="list"),
    # 课程详情页
    re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),

]
