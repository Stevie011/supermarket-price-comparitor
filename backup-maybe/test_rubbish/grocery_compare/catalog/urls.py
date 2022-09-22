from django.urls import path
from . import views
from django.urls import re_path
from django.contrib import admin
#from article import urls
#from django.conf.urls import url, include


urlpatterns = [
    path("",views.index, name="index"),
    #re_path(r'^admin/', admin.site.urls),
]
