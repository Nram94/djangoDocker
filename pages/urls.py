from django.urls import path
from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductCreateSuccessView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/product-created', ProductCreateSuccessView.as_view(), name='product-created'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    
]