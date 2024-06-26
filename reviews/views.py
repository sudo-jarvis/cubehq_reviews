"""Module containing Django views for the [project/app name] app."""

from django.db.models import Avg, Count, F, OuterRef, Subquery
from rest_framework.generics import ListAPIView
from rest_framework.pagination import CursorPagination

from reviews.models import Metadata, ReviewHistory
from reviews.serializers import TopCategorySerializer, ReviewDetailsSerializer


class ReviewTrendView(ListAPIView):
    """Lists Top Review Categories."""

    serializer_class = TopCategorySerializer
    queryset = Metadata.objects

    def filter_queryset(self, queryset):
        """Filter top 5 categories with total review count, average stars."""
        top_category_count = 5  # No. of top categories to be filtered

        # Gets the latest review for a particular review_id
        latest_review_subquery = (
            ReviewHistory.objects.filter(review_id=OuterRef("review__review_id"))
            .order_by("-created_at")
            .values("id")[:1]
        )

        # Logic to get top categories based on average star rating
        top_categories_queryset = (
            queryset.filter(review_id=Subquery(latest_review_subquery))
            .values(
                "category_id",
                name=F("category__name"),
                description=F("category__description"),
            )
            .annotate(
                average_stars=Avg("review__stars"),
                total_reviews=Count("review")
            )
            .order_by("-average_stars")[:top_category_count]
        )
        # This took a total of 2 django ORM queries(Including 1 Subquery)
        return top_categories_queryset


class ReviewSearchPagination(CursorPagination):
    """Sets pagination parameters for filtering reviews."""

    page_size = 15
    ordering = "-created_at"


class CategoryReviewView(ListAPIView):
    """Lists reviews filtered by a provided category ID."""

    pagination_class = ReviewSearchPagination
    queryset = Metadata.objects
    serializer_class = ReviewDetailsSerializer

    def filter_queryset(self, queryset):
        """
        Filter the queryset based on a 'category_id' query parameter.

        If category_id is not present, returns all reviews
        """
        category_id = self.request.GET.get("category_id")
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
            # This took 1 django ORM query

        return queryset.annotate(created_at=F("review__created_at"))
