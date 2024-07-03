from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_transactions/', views.get_transactions, name='get_transactions'),
]
