from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'/queue', views.QueueViewSet)
router.register(r'/makanan', views.MakananViewSet)
router.register(r'/merchant', views.MerchantViewSet)
router.register(r'/quotes', views.QuotesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
