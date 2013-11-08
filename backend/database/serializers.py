
from database.models import Family, Breed
from rest_framework import serializers


## Breeds

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family


class BreedSerializer(serializers.ModelSerializer):
    family  = serializers.HyperlinkedRelatedField(many=True, view_name='family-detail', read_only=True)
    related = serializers.HyperlinkedRelatedField(many=True, view_name='breed-detail',  read_only=True)

    class Meta:
        model = Breed
