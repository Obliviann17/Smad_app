from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    available = models.BooleanField(default=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    card_number = models.CharField(max_length=16, default=None)
    cvv_code = models.CharField(max_length=3, default=None)
    validity = models.CharField(max_length=5, default=None)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Замовлення"
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return 'Замовлення {}'.format(self.id)
