from django.db import models

# Create your models here.

class Order(models.Model):
    pruser = models.ForeignKey('pruser.Pruser', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product',on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    
    def __str__(self):
        return self.pruser # 누군지 나타내주는 코드
    class Meta:
        db_table = 'project_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'