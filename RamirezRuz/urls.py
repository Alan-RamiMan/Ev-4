from rest_framework import routers
from .api import CarrerasViewSet


router=routers.DefaultRouter()

router.register('api/crud',CarrerasViewSet,'crud')


urlpatterns = router.urls
