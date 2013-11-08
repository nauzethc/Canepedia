
from django.forms import widgets
from rest_framework import serializers
from adoptions.models import Dog, Brood


## Dogs

class DogSerializer(serializers.ModelSerializer):
    breed   = serializers.HyperlinkedRelatedField(many=True, view_name='breed-detail', read_only=True)
    related = serializers.HyperlinkedRelatedField(many=True, view_name='dog-detail', read_only=True)

    class Meta:
        model = Dog


class BroodSerializer(serializers.ModelSerializer):
    breed   = serializers.HyperlinkedRelatedField(many=True, view_name='breed-detail', read_only=True)
    related = serializers.HyperlinkedRelatedField(many=True, view_name='dog-detail', read_only=True)

    class Meta:
        model = Brood