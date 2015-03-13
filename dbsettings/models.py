from django.db import models
from django.contrib.sites.models import Site


class SettingManager(models.Manager):
    def get_queryset(self):
        all = super(SettingManager, self).get_queryset()
        return all.filter(site=Site.objects.get_current())

class Setting(models.Model):
    site = models.ForeignKey(Site)
    module_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255, blank=True)
    attribute_name = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True)

    objects = SettingManager()
    all_sites = models.Manager()


    class Meta:
        unique_together = ('site', 'module_name', 'class_name', 'attribute_name')


    def __nonzero__(self):
        return self.pk is not None

    def save(self, *args, **kwargs):
        if not self.site_id:
            self.site = Site.objects.get_current()
        return super(Setting, self).save(*args, **kwargs)
