
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CatViewSet, OwnerViewSet, ToyViewSet
router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register('toys', ToyViewSet)

urlpatterns = [
    # path('cats/<int:pk>/', CatDetail.as_view()),
    # path('cats/', CatListApi.as_view()),
       path('', include(router.urls)),
]