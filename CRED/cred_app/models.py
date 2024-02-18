from django.db import models

# Create your models here.

class Stocks(models.Model):
    id = models.AutoField(primary_key=True, serialize=True, null=False)
    stock_name = models.CharField(max_length=100, null=False)
    stock_price = models.IntegerField(null=False)

    class Meta:
        db_table = 'stock_prices'

