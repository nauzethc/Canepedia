
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics

from database.models import Family, Breed, FCIGroupSection
from database.serializers import FamilySerializer, BreedSerializer, FCIGroupSectionSerializer, BreedListSerializer


## Breeds

class FCIGroupList(generics.ListCreateAPIView):
    '''
    List all FCI groups
    '''
    queryset         = FCIGroupSection.objects.all()
    serializer_class = FCIGroupSectionSerializer


class FamilyList(generics.ListCreateAPIView):
    '''
    List all breed families, or create new one
    '''
    queryset         = Family.objects.order_by('group', 'section')
    serializer_class = FamilySerializer


class FamilyDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update or delete a breed family
    '''
    queryset         = Family.objects.all()
    serializer_class = FamilySerializer


class BreedList(generics.ListCreateAPIView):
    '''
    List all breeds, or create new one
    '''
    queryset         = Breed.objects.all()
    serializer_class = BreedListSerializer


class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update or delete a breed
    '''
    queryset         = Breed.objects.all()
    serializer_class = BreedSerializer
