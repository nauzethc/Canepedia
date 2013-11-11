
from database.models import Family, Breed
from rest_framework import serializers


## Breeds

class FamilyRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ('id', 'name', )


class BreedRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name', )


class FamilySerializer(serializers.ModelSerializer):
    breeds = BreedRelatedSerializer(many=True)
    class Meta:
        model = Family


class BreedSerializer(serializers.ModelSerializer):
    #family  = serializers.HyperlinkedRelatedField(many=True, view_name='family-detail', read_only=True)
    #related = serializers.HyperlinkedRelatedField(many=True, view_name='breed-detail',  read_only=True)
    family  = FamilyRelatedSerializer(many=True)
    related = BreedRelatedSerializer(many=True)

    class Meta:
        model = Breed
