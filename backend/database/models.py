
from django.db import models
from django.template.defaultfilters import slugify



## FCI

class FCIGroup(models.Model):
    group       = models.IntegerField(unique=True, primary_key=True)
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return "Grupo %i: %s" % (self.group, self.description)


class FCIGroupSection(models.Model):
    group       = models.ForeignKey(FCIGroup)
    section     = models.IntegerField(default=1)
    description = models.CharField(max_length=100)

    class Meta:
        unique_together = ('group', 'section')

    @property
    def name(self):
        return "%i.%i %s" % (self.group.group, self.section, self.description)

    def __unicode__(self):
        return self.name



## Breeds

class Family(models.Model):
    name      = models.CharField(max_length=50)
    slug      = models.SlugField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = "Families"

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Family, self).save(*args, **kwargs)



class Breed(models.Model):
    name      = models.CharField(max_length=50)
    slug      = models.SlugField(max_length=50, null=True)
    origin    = models.CharField(max_length=50, blank=True)
    group     = models.ForeignKey(FCIGroupSection)
    related   = models.ManyToManyField('self', symmetrical=True, blank=True, null=True)
    wikipedia = models.URLField(blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Breed, self).save(*args, **kwargs)

    def get_group_name(self):
        return self.group.__unicode__()
