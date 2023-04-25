from rest_framework import  viewsets
from .serializers import CatSerializer, OwnerSerializer, ToySerializer
from .models import Cat, Owner, Toy


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.filter(is_purebred=True, deleted = None).order_by('-created')
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer