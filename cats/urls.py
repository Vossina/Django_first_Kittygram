
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CatViewSet, OwnerViewSet # CatList, CatDetail # Cat_detail, CatApiList
router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
urlpatterns = [
    # path('cats/<int:pk>/', CatDetail.as_view()),
    # path('cats/', CatListApi.as_view()),
       path('', include(router.urls)),
]