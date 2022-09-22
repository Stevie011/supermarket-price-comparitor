from django.urls import path
from . import views

urlpatterns =[
    path("", views.index,name="compare"),
    path("add-compare", views.add_compare, name="add-compare")

]