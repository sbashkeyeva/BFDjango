from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Restaurant(models.Model):
    name = models.TextField(blank=True, null=True)
    number = models.IntegerField()
    telephone = models.IntegerField()
    city = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    rating = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.rating


class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant
