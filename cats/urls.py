
from django.urls import path

from .views import Cat_list, Cat_detail, CatApiList

urlpatterns = [
    path('cats/<int:pk>/', Cat_detail),
    path('cats/', CatApiList.as_view()),
]