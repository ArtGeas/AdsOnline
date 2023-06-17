from django.urls import include, path
from rest_framework import routers

from ads.views import AdViewSet, CommentViewSet

# TODO настройка роутов для модели


urlpatterns = [
    path('<pk>/comments/', CommentViewSet.as_view())
]

router = routers.SimpleRouter()
router.register('', AdViewSet)
urlpatterns += router.urls


