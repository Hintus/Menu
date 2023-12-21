from django.urls import reverse

from django.db import models


# Create your models here.

class ModelMenu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    parent = models.ForeignKey(verbose_name=u'Родительское меню', to='self', blank=True, null=True,
                               related_name='children', on_delete=models.CASCADE)
    another_menu = models.ForeignKey(verbose_name=u'Отобразить на этой странице', to='self', blank=True,
                                     null=True, related_name='Menu', on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('menu_url', kwargs={'menu_name': self.name})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
