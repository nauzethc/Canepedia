
from django import forms
from database.models import Breed, Family, FCIGroupSection


class FamilyAdminForm(forms.ModelForm):
    class Meta:
        model = Family


class BreedAdminForm(forms.ModelForm):
    class Meta:
        model = Breed

    def __init__(self, *args, **kwargs):
        super(BreedForm, self).__init__(*args, **kwargs)
        self.fields['related'].queryset = Breed.objects.exclude(id__exact=self.instance.id)
