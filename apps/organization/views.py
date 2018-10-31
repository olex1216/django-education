# encoding: utf-8
from django.shortcuts import render

from django.views.generic.base import View
from .models import CourseOrg, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# 处理课程机构列表的view
class OrgView(View):
    def get(self, request):

        # 查找到所有的课程机构
        all_orgs = CourseOrg.objects.all()
        # 总共有多少家机构使用count进行统计
        org_nums = all_orgs.count()
        # 热门机构,如果不加负号会是有小到大。
        # hot_orgs = all_orgs.order_by("-click_nums")[:3]

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        # 取出所有的城市
        all_city = CityDict.objects.all()
        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_city": all_city,
            "org_nums": org_nums,
        })
