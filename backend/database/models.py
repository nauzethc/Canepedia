
from django.db import models
from django.template.defaultfilters import slugify


## Breeds

class Family(models.Model):
    name      = models.CharField(max_length=50)
    slug      = models.SlugField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = "Families"

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Family, self).save(*args, **kwargs)


class Breed(models.Model):
    name      = models.CharField(max_length=50)
    slug      = models.SlugField(max_length=50, null=True)
    origin    = models.CharField(max_length=50, blank=True)
    family    = models.ManyToManyField(Family)
    related   = models.ManyToManyField('self')
    wikipedia = models.URLField(blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Breed, self).save(*args, **kwargs)