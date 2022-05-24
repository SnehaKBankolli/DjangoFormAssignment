from django.urls import path,re_path

from . import views

app_name='polls'
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'',views.wrong_url,name='error'),
]