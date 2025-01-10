from django.urls import path
from . import views
urlpatterns = [
    path('plot',views.bar_chart_view,name='Plot')
]