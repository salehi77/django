from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.core import exceptions
User = get_user_model()





class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='categories')
    imageAlt = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subcat')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        current = self.parent
        while current != None:
            if current.id == self.id:
                raise exceptions.ValidationError('You can\'t have yourself as a parent!')
            current = current.parent

        return super(Category, self).save(*args, **kwargs)



class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='products')


    def __str__(self):
        return self.title
