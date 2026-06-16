from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=120, null = False, blank = False)
    rating = models.DecimalField(decimal_places=2, max_digits=2)
    photo = models.ImageField(upload_to = "profile/images/", null = False, blank = False)
    about = models.TextField()
    age = models.IntegerField()
    #user_id
