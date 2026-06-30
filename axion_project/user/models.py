from django.db import models


# Create your models here.

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=11, decimal_places=2, default=0.0)
    telegram_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.email}, {self.status}"


class Profile(models.Model):
    username = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    age = models.IntegerField(null=False, blank=False)
    about = models.TextField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="static/media/images")
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}, {self.user_id}"
