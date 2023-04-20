
from django.urls import path

from .views import CatList, CatDetail # Cat_detail, CatApiList

urlpatterns = [
    path('cats/<int:pk>/', CatDetail.as_view()),
    path('cats/', CatList.as_view()),
]