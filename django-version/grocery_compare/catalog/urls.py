from django.urls import path
from . import views
from django.urls import include, re_path
from django.contrib import admin
from article import urls

urlpatterns = [
    path("",views.index, name="index"),
    re_path(r'^admin/', admin.urls),
]
