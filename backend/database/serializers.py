
from database.models import Family, Breed, FCIGroupSection, FCIGroup
from rest_framework import serializers


## Breeds

class FCIGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FCIGroup
        fields = ('group', 'description')


class FCIGroupSectionRelatedSerializer(serializers.ModelSerializer):
    group = FCIGroup
    name  = serializers.CharField()
    class Meta:
        model = FCIGroupSection
        fields = ('section', 'name', 'group' )


class FCIGroupSectionSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = FCIGroupSection
        fields = ('id', 'name')


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
    #family  = FamilyRelatedSerializer(many=True, required=False)
    group   = serializers.CharField(source='get_group_name', read_only=True)
    related = BreedRelatedSerializer(many=True, required=False)

    class Meta:
        model = Breed
