from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery")
    link = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.title


class Work(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    description2 = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery")
    link = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.title

#model for the items in the drop down list
class Item(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name


#items = ["Brown Bread (loaf)", "2 litre fresh milk", "Tuna (tin)", "Toilet paper (24)", "Doritos Sweet Chili 145g", "Strawberries 250g", "Baked Beans (tin)", "White hambu
   #...: rger rolls (6)", "Lettuce Head", "Spaghetti (500g)", "Button Mushrooms (250g)"]