# 路由
# 1、url(r'^index/', views.index),
# url(r'^home/', views.Home.as_view()),
# 2、url(r'^detail-(\d+).html', views.detail),
# 3、url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail)
#
# PS:
#     def detail(request, *args, **kwargs):
#         pass
#
#
# 实战：
# a.
#     url(r'^detail-(\d+)-(\d+).html', views.detail),
#
#
#     def func(request, nid, uid):
#         pass
#
#
#     def func(request, *args):
#         args = (2, 9)
#
#
#     def func(request, *args, **kwargs):
#         args = (2, 9)
#
#
# b.
#     url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail)
#
#
#     def func(request, nid, uid):
#         pass
#
#
#     def funct(request, **kwargs):
#         kwargs = {'nid': 1, 'uid': 3}
#
#
#     def func(request, *args, **kwargs):
#         args = (2, 9)



# 4、 name
# 对URL路由关系进行命名， ** ** *以后可以根据此名称生成自己想要的URL ** ** *

#     url(r'^asdfasdfasdf/', views.index, name='i1'),
#     url(r'^yug/(\d+)/(\d+)/', views.index, name='i2'),
#     url(r'^buy/(?P<pid>\d+)/(?P<nid>\d+)/', views.index, name='i3'),

#
#     def func(request, *args, **kwargs):
#         from django.urls import reverse
#
#         url1 = reverse('i1')  # asdfasdfasdf/
#         url2 = reverse('i2', args=(1, 2,))  # yug/1/2/
#         url3 = reverse('i3', kwargs={'pid': 1, "nid": 9})  # buy/1/9/


#         {% url "i1" %}               # asdfasdfasdf/
#         {% url "i2" 1 2 %}           # yug/1/2/
#         {% url "i3" pid=1 nid=9 %}   # buy/1/9/
#
#         注：
# 			# 当前的URL
# 			request.path_info

# 在views里面可以通过reverse 来生成URL
# import django.urls import reverse
# url = reverse(’indexx',args=(90,))
# url = reverse(’indexx',kwargs={'nid':'1',})
















