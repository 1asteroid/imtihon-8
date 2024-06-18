from django.db import models
from django.contrib.auth.models import User
from.helpes import SaveImages, SaveImagesTeam, SaveImagesBlog


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    image = models.ImageField(upload_to=SaveImages.product_images_path)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['slug'])
        ]

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveBigIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]
        indexes = [
            models.Index(fields=['id'])
        ]


class Team(models.Model):
    full_name = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveImagesTeam.team_images_path)

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.full_name


class Blog(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to=SaveImagesBlog.blog_images_path)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name
