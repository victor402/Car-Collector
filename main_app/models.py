from django.db import models
from django.urls import reverse

GASES = (
    ('D', 'Diesel'),
    ('N', 'Normal gas'),
    ('E', 'Electricity'),
    ('P', 'propane')
)

# Create your models here.

class DetailShop(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail_shops_detail', kwargs={'pk': self.id})


class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    year = models.IntegerField('year')
    detail_shops = models.ManyToManyField(DetailShop)




    def _str_(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Gassing(models.Model):
    date = models.DateField('gassing date')
    gas = models.CharField(max_length=1, choices=GASES, default=GASES[0][0])
    car = models.ForeignKey(Car, on_delete=models.CASCADE)




    def _str_(self):
        return f"{self.get_gas_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    
