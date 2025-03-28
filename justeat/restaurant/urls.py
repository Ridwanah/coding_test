from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant_list/<str:postcode>/', views.PostcodeView.as_view(), name='restaurant_list')
]