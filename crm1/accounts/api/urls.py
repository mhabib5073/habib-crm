from django.urls import path
from accounts.api import views


urlpatterns = [
    
    path('customer-api/', views.CustomerListView.as_view()),
    path('customer-api/<int:pk>/', views.customerView.as_view()),
    path('product-api/', views.productListView.as_view()),
    path('product-api/<int:pk>/', views.productView.as_view()),
    path('order-api/', views.orderListView.as_view()),
    path('order-api/<int:pk>/', views.orderView.as_view()),
]