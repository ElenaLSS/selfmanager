<<<<<<< HEAD
from django.conf.urls import url
=======
from django.urls import path
>>>>>>> upstream/master

from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.index, name='index'),
=======
    path('', views.index, name='index'),
    path('addtask/', views.add_task),
>>>>>>> upstream/master
]