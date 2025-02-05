from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    item_price = models.IntegerField()
    item_image = models.URLField(max_length=2000)

    def __str__(self):
        return self.item_name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()

    def __str__(self):
        return self.name