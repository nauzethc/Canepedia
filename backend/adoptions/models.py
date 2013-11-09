
from django.db import models
from database.models import Breed


## Dogs

class Dog(models.Model):
    name       = models.CharField(max_length=50)
    breed      = models.ManyToManyField(Breed)
    crossbreed = models.BooleanField(default=False)
    birth      = models.DateField(null=True, blank=True)
    related    = models.ManyToManyField('self')
    info       = models.TextField(blank=True)

    def __unicode__(self):
        '''
        Returns 'crossbreed' if it's true,
        first breed name otherwise
        '''
        if self.pk:
            if self.crossbreed:
                return '%s, %s' % (self.name, 'Crossbreed')
            elif self.breed.count() > 0:
                return '%s, %s' % (self.name, self.breed.first().name)
        elif self.name:
            return self.name
        return 'Unknown'


## Groups

class Brood(models.Model):
    breed      = models.ManyToManyField(Breed)
    crossbreed = models.BooleanField(default=False)
    birth      = models.DateField(null=True)
    related    = models.ManyToManyField(Dog)

    def __unicode__(self):
        '''
        Returns 'crossbreed' if it's true,
        first breed name otherwise
        '''
        if self.pk:
            if self.crossbreed:
                return '%s, %s' % (self.name, 'Crossbreed')
            elif self.breed.count() > 0:
                return '%s, %s' % (self.name, self.breed.first().name)
        return 'Unknown'
