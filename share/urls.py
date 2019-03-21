from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views 



urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^signup/',views.signup,name="signup"),
    url(r'^profile/',views.profile,name="profile"),
    url(r'^login_user/',views.login_user,name="login_user"),
    url(r'^user_logout/',views.user_logout,name="user_logout"),
    #url(r'^([\w-]+){4}[10-100]/',views.fetch_view,name="fetch_view"),
    url(r'^\w+/',views.fetch_view,name="fetch_view"),
    url(r'^home_afterlogin',views.home_afterlogin,name='home_afterlogin'),
]