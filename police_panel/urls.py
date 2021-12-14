from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='Home'),
    path('register/', views.register, name="register"),
    path('view/', views.view_reports, name="all-complaints"),
]