from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('police/', include('police_panel.urls')),
    path('public/', include('user_panel.urls')),
]
