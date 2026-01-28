"""
URL configuration for ojaoba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from productApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.getHome, name="home"),
    path('products/', views.getProducts, name='products'),
    path('products/<int:product_id>/', views.getProductById, name='get_product'),
    path('addproduct/', views.addProduct, name='add_product'),
    path('products/<int:product_id>/addfeature/', views.addFeature, name='add_feature'),
    path('edit-product/<int:product_id>/', views.editProduct, name='edit-product'),
    path("delete-product/<int:product_id>/", views.deleteProduct, name="delete-product"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)