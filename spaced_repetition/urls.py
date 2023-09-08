from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('apps.users.urls')),
    path('api/v1/decks/', include('apps.decks.urls', namespace='decks')),
    path('api/v1/cards/', include('apps.cards.urls')),
]
