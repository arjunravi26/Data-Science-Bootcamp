from crud import views
from django.urls import path

urlpatterns = [
    path('index',view=views.home,name='index'),
    path('display',view=views.display,name='display'),
    path('delete',view=views.delete,name='delete'),
]
