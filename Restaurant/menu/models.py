from django.db import models

# Create your models here.


class Menu(models.Model):

    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


class MenuItem(models.Model):

    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    is_vegetarian = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.id} - {self.name} ({self.menu.name})"

