
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics

from adoptions.models import Dog, Brood
from adoptions.serializers import DogSerializer, BroodSerializer


## Dogs

class DogList(generics.ListCreateAPIView):
    '''
    List all dogs, or create new one
    '''
    queryset         = Dog.objects.all()
    serializer_class = DogSerializer


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update or delete a breed
    '''
    queryset         = Dog.objects.all()
    serializer_class = DogSerializer


class BroodList(generics.ListCreateAPIView):
    '''
    List all broods, or create new one
    '''
    queryset         = Brood.objects.all()
    serializer_class = BroodSerializer

class BroodDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update or delete a breed
    '''
    queryset         = Brood.objects.all()
    serializer_class = BroodSerializer
