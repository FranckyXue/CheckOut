from django.urls import path

from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.library_list, name='library_list'),
    path('library/<int:library_id>/', views.library_detail, name='library_detail'),
    # 添加其他相关URL配置
]
