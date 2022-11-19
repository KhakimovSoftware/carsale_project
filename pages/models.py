from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class BannerModel(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'))
    description = models.CharField(max_length=100, verbose_name=_('description'))
    image = models.ImageField(upload_to='banners/', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
