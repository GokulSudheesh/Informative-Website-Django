from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    organization = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=16, unique=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)


class Find(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    find_us = models.CharField(max_length=100)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=280)

    def __str__(self):
        return self.review

