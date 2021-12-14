from django.conf.urls import url
from . import views
from django.urls import include, path
urlpatterns = [
    path('', views.index, name='Home'),
    path('register/', views.registerUser, name="RegisterUser"),
    path('login/', views.login, name="Login"),
    path('logout/', views.logout, name="Logout"),
    path('create_complaint/', views.create_complaint, name="Complaint"),
]