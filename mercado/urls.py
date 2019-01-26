from rest_framework import routers
from rest_framework import viewsets

from django.contrib import admin
from django.urls import path, include
from accounts.views import UserViewSet
from produto.views import ProdutoViewSet
from compra.views import CompraViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProdutoViewSet)
router.register(r'compras', CompraViewSet, 'compras')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
]
