from django.db import models
from datetime import datetime
from django.db.models import ForeignKey


class User(models.Model):
    pass

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    discount = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="media/images", null=False, blank=False)

    def __str__(self): 
        return self.name

class Goods(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    creator = ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    discount = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="media/images/", null=False, blank=False)
    video = models.FileField(upload_to="media/video/", null=False, blank=False)
    release = models.DateTimeField(default=datetime.now)
    file = models.FileField(upload_to="goods_files/", null=False, blank=False)


class Game(Goods):

    pass

class Skin(Goods):

    GRADES = {
        "UC": "Uncommon",
        "CM": "Common",
        "RR": "Rare",
        "SR": "Superrare",
        "EP": "Epic",
        "MT": "Mythic",
        "AC": "Arcane",
        "LG": "Legend",
    }
    grade = models.CharField(max_length=2, choices=GRADES, default="UC")