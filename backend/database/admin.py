
from django.contrib import admin
from database.models import Family, Breed, FCIGroup, FCIGroupSection
from database.forms import BreedAdminForm, FamilyAdminForm



## FCI

class FCIGroupAdmin(admin.ModelAdmin):
    list_display = ('group', 'description', )
    ordering = ('group', )


class FCIGroupSectionAdmin(admin.ModelAdmin):
    extra = 3
    list_display = ('group', 'section', 'description', )
    ordering = ('group', 'section', )




## Breeds

class FamilyAdmin(admin.ModelAdmin):
    form = FamilyAdminForm
    prepopulated_fields = { 'slug': ('name', ), }


class BreedAdmin(admin.ModelAdmin):
    form = BreedAdminForm
    prepopulated_fields = { 'slug': ('name', ), }



admin.site.register(FCIGroup, FCIGroupAdmin)
admin.site.register(FCIGroupSection, FCIGroupSectionAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Breed, BreedAdmin)