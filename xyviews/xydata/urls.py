from django.urls import path
from xyviews.xydata import views

urlpatterns = [
    path("", views.index, name="home"),  # 主页
    path("uni-list/", views.uni_list, name="uni_list"),  # 列表页
    path("university/<str:name>.html", views.uni_detail, name="uni_detail"),  # 详情页
]
