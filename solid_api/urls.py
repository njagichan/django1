from django.urls import path
from . import views 

urlpatterns = [
    path(r"drinks/",views.drinks, name="drinks"),
    path(r"addDrinks/",views.addDrinks,name="add"),
    path(r"drinks/<int:id>/",views.changeDrinks,name="change")
]