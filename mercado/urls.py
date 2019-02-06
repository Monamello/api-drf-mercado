from rest_framework import routers
from rest_framework import viewsets

from django.contrib import admin
from django.urls import path, include
from accounts.views import UserViewSet, UserCompraViewSet
from produto.views import ProdutoViewSet
from compra.views import CompraViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')
# router.register(r'ativos', UserCompraViewSet)
router.register(r'products', ProdutoViewSet)
router.register(r'compras', CompraViewSet, 'compras')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/ativos', UserCompraViewSet.as_view({'get': 'list'})),
    path('', include('rest_framework.urls', namespace='rest_framework')),
]
