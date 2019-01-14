from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Категории товаров"""
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')
    slug = models.SlugField(max_length=100)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара"""
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    price = models.IntegerField("Цена", default=0)
    slug = models.SlugField(max_length=150)
    availability = models.BooleanField("Наличие", default=True)
    quantity = models.IntegerField("Количество", default=1)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


class CartItem(models.Model):
    """Модель выбраных продуктов"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)


    def __unicode__(self):
        return "Cart item for product {0}".format(self.product.title)


class Cart(models.Model):
    """Модель корзины"""
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __unicode__(self):
        return str(self.id)

