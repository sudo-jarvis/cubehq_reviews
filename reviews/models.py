from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ReviewHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=2048, null=True)
    stars = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    review_id = models.CharField(max_length=255)
    created_at = models.DateTimeField()


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()


class Metadata(models.Model):
    id = models.BigAutoField(primary_key=True)
    tone = models.CharField(max_length=255, null=True)
    sentiment = models.CharField(max_length=255, null=True)
    review = models.OneToOneField(ReviewHistory, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
