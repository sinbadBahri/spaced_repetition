from rest_framework import routers
from .views import CardViewSet

router = routers.DefaultRouter()
router.register(r'', CardViewSet)
urlpatterns = router.urls
