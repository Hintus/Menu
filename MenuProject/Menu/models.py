from django.urls import reverse

from django.db import models

# Create your models here.

class ModelMenu(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(verbose_name=u'Родительское меню', to='self', blank=True, null=True,
                               related_name='children', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('menu_url', kwargs={'menu_name': self.name})

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
