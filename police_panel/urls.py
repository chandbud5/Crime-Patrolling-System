from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='Home'),
    # path('register/', views.register, name="register"),
    path('view/', views.view_complaints, name="all-complaints"),
    path('report/<str:id>', views.report),
    path('accept/<str:id>', views.complaint_accepted),
]