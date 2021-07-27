from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage),
    url(r'^candidates/', include('candidates.urls')),
]
