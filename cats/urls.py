
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CatViewSet, OwnerViewSet, ToyViewSet, LightCatViewSet
router = DefaultRouter()
router.register(r'cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register('toys', ToyViewSet)
router.register(r'my-cats', LightCatViewSet)
urlpatterns = [
    # path('cats/<int:pk>/', CatDetail.as_view()),
    # path('cats/', CatListApi.as_view()),
       path('', include(router.urls)),
]