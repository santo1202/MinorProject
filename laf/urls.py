from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report, name='report'),
    path('found/', views.found, name='found'),
    path("view/", views.view, name='view'),   
]

