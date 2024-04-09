"""Module containing Django serializers for the reviews app."""

from rest_framework import serializers

from .models import Category, Metadata, ReviewHistory


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for the ReviewHistory model."""

    class Meta:
        """Configuration for the ReviewSerializer."""

        model = ReviewHistory
        fields = '__all__'


class ReviewDetailsSerializer(serializers.ModelSerializer):
    """Serializer for Review Details related to the metadata."""

    review = ReviewSerializer()

    class Meta:
        """Configuration for the ReviewDetailsSerializer."""

        model = Metadata
        fields = ('tone', 'sentiment', 'category_id', 'review')


class TopCategorySerializer(serializers.ModelSerializer):
    """Serializer for the Category model, with aggregated review statistics."""

    average_stars = serializers.FloatField()
    id = serializers.CharField(source='category_id')
    total_reviews = serializers.IntegerField()

    class Meta:
        """Configuration for the TopCategorySerializer."""

        model = Category
        fields = ('id', 'name', 'description',
                  'average_stars', 'total_reviews')
