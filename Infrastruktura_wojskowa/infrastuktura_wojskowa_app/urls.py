from django.urls import path, include
from .views import  index
from rest_framework import routers

from infrastuktura_wojskowa_app import views

router = routers.DefaultRouter()
router.register(r'personel', views.PersonelView)
router.register(r'adres', views.AdresView)
router.register(r'pododdzial', views.PododdzialView)
router.register(r'oddzialy', views.OddzialyView)
router.register(r'operacyjne', views.Zwiazki_operacyjneView)
router.register(r'taktyczne', views.Zwiazki_taktyczneView)
router.register(r'stopien', views.StopienView)
router.register(r'baza', views.BazaView)


urlpatterns = [
    path('xd/', include(router.urls)),
    path('', index, name='index_name'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

