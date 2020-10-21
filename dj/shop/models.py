from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class DateTimes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(DateTimes):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='categories')
    imageAlt = models.CharField(max_length=255)

    parent = models.ForeignKey('self', null=True, blank=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Product(DateTimes):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    imageAlt = models.CharField(max_length=255)
    discount = models.DecimalField(
        max_digits=5, decimal_places=2,
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    price = models.PositiveIntegerField()
    # rate = models.DecimalField(max_digits=3, decimal_places=2)
    # reviews = models.PositiveIntegerField()

    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
