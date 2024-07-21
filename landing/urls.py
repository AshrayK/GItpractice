from django.urls import path
from . import views

app_name='landing'
urlpatterns=[
    path("",views.index,name='index'),
    path("available/",views.available,name='available'),
    path("<str:name>",views.greet,name='greet'),
]