from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.core import exceptions
from django.utils.text import slugify
from django.db.models import Avg, Count, Max, Min
User = get_user_model()





class Category(models.Model):
    title = models.CharField(max_length=255)
    slug_title = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()
    imageAlt = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subcat')
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='categories')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        current = self.parent
        while current != None:
            if current.id == self.id:
                raise exceptions.ValidationError('You can\'t have yourself as a parent!')
            current = current.parent

        self.slug_title = slugify(self.title, allow_unicode=True)

        return super(Category, self).save(*args, **kwargs)



class Product(models.Model):
    title = models.CharField(max_length=255)
    slug_title = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()
    imageAlt = models.CharField(max_length=255)
    discount = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='products')
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='products')

    @property
    def average_rate(self):
        # avg = self.rates.aggregate(Avg('rate'))['rate__avg']
        # return avg if avg else 0
        return self.rates.aggregate(Avg('rate'))['rate__avg']

    @property
    def count_reviews(self):
        return self.rates.exclude(review='').aggregate(Count('review'))['review__count']

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug_title = slugify(self.title, allow_unicode=True)
        return super(Product, self).save(*args, **kwargs)


# class ProductDetail(models.Model):
#     size
#     gender
#     color
#     material
#     insole






class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rates')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rates')
    rate = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    review = models.TextField(null=True, blank=True, default='')

    class Meta:
        unique_together = ['user', 'product']


    def __str__(self):
        return '%s, %s, %d' % (self.user, self.product, self.rate)
