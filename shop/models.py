from django.db import models

# Create your models here.

class Products(models.Model):
    slug = models.CharField(max_length=100 , null=False , blank=False)
    name = models.CharField(max_length=100 , null=False , blank=False)
    description = models.TextField(null=False , blank=False)
    image = models.ImageField(upload_to='img/%y/%m/%d' , null=False , blank=False)
    price = models.FloatField(null=False , blank=False)
    stock = models.IntegerField(default=1)
    created_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    