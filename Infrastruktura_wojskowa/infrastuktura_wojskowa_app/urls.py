from django.urls import path, include
from .views import  index
from rest_framework import routers

from infrastuktura_wojskowa_app import views

router = routers.DefaultRouter()
router.register(r'personel', views.PersonelView)
router.register(r'adres', views.AdresView)


urlpatterns = [
    path('xd/', include(router.urls)),
    path('', index, name='index_name'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

