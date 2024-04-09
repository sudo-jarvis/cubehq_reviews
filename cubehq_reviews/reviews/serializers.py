from rest_framework import serializers

from .models import Category, Metadata, ReviewHistory


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewHistory
        fields = '__all__'

class LatestReviewSerializer(serializers.ModelSerializer):
    review = ReviewSerializer()
    
    class Meta:
        model = Metadata
        fields = ('tone', 'sentiment', 'category_id', 'review')


class TopCategorySerializer(serializers.ModelSerializer):
    average_stars = serializers.FloatField()
    id = serializers.CharField(source='category_id')
    total_reviews = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'average_stars', 'total_reviews')
        