from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path("products", views.ProductListView.as_view(), name="store_home"),
    path("category", views.CategoryListView.as_view(), name="categories"),
    path("product/<slug:slug>", views.Product.as_view(), name="product"),
    path(
        "category/<slug:slug>", views.CategoryItemView.as_view(), name="category_item"
    ),
    path("order/<int:int>", views.OrderListView.as_view(), name="order"),
]
