from django.urls import path
from MyApp import views

urlpatterns = [

    # path('', views.print_hello),
    path('create', views.create, name='create'),
    path('edit', views.edit, name='edit'),
    path('list', views.list, name='list'),
]
