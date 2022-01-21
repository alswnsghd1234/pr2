from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='삼품설명')
    stuck = models.IntegerField(verbose_name='재고')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    
    def __str__(self):
        return self.name # 누군지 나타내주는 코드

    class Meta:
        db_table = 'project_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'