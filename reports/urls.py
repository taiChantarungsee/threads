from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('district', views.district_view, name='district'),
]