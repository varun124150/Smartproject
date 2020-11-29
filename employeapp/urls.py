from django.urls import path
from .views import home,show,add


urlpatterns = [
 
    path('home/',home,name="home"),
    path("show/",show,name="show"),
    path("add/",add,name="add")

]

