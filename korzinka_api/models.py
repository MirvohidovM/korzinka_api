from django.db import models

class Mahsulotlar(models.Model):
    title = models.CharField(verbose_name='Mahsulot Nomi', max_length=50)
    parent = models.ForeignKey('Mahsulot_Turi', on_delete=models.PROTECT)
    date = models.DateTimeField(verbose_name='Keltirilgan Sanasi', auto_now_add=True)
    class Meta:
        verbose_name = 'mahsulot'
        verbose_name_plural = 'mahsulotlar'
        ordering = ['-date']

    def __str__(self):
        return self.title

class Mahsulot_Turi(models.Model):
    title = models.CharField(verbose_name='Mahsulot Turi', max_length=150)

    class Meta:
        verbose_name = 'mahsulot turi'
        verbose_name_plural = 'mahsulot turlari'

    def __str__(self):
        return self.title
