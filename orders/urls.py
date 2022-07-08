from django.urls import path
from . import views

app_name = "orders"
urlpatterns = [
    path("order", views.CreateOrderView.as_view(), name="orders")
    # path("/order/<int:pk>", views.OrderDetailView.as_view(), name="order_detail"),'),
]
