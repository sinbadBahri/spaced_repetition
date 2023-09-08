from rest_framework import routers
from .views import CardViewSet

router = routers.DefaultRouter()
router.register(prefix=r'', viewset=CardViewSet)
urlpatterns = router.urls
