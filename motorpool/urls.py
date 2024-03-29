from django.urls import path
from . import views

app_name = 'motorpool'

urlpatterns = [
    path('index/', views.index),
    path('brand-list/', views.brand_list, name='brand_list'),
    path('brand-detail/<int:pk>/', views.brand_detail, name='brand_detail')
]

