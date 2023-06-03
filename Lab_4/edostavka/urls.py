from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path(r'^book/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product-detail'),
]
