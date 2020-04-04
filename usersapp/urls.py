from django.urls import path,include
from . import views
from . import api
from rest_framework import routers
router=routers.DefaultRouter()
router.register('',api.userviewset)
urlpatterns=[
    path('',views.user_list,name='userlist'),
    path('userdetail/<str:user_id>/',views.user_detail),
    path('home',views.home,name='home'),
    path('delete/<str:user_id>/',views.delete_user),
    path('user/',include(router.urls)),
    path('userapiview',api.Userapiview.as_view()),
    path('update/<str:user_id>/',api.updateapi.as_view())

]