from . import views
from django.conf.urls import url

urlpatterns = [
    #url('^/?$',views.index),
    url('^index$',views.index,name='index'),
    url('^list/(\d+)?/?(\d+)?$',views.list,name="list"),  #第一个括号为分类，第二个括号为页码
    url('^detail/(\d+)$',views.detail,name='detail')
]

# 大分类_小分类_品牌_页码