from django.db.models import Avg, Count, F, OuterRef, Subquery
from rest_framework.generics import ListAPIView
from rest_framework.pagination import CursorPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Metadata, ReviewHistory
from .serializers import TopCategorySerializer, LatestReviewSerializer


class ReviewTrendView(APIView):
    def get(self, request):
        top_categories = (
            Metadata.objects.filter(
                review_id=Subquery(
                    ReviewHistory.objects.filter(id=OuterRef("review_id"))
                    .order_by("-created_at")
                    .values("id")[:1]
                )
            )
            .values('category_id', name=F('category__name'), description=F('category__description'))
            .annotate(average_stars=Avg("review__stars"), total_reviews=Count("review"))
            .order_by("-average_stars")
        )
        print(top_categories)
        serializer = TopCategorySerializer(top_categories, many=True)
        return Response(serializer.data)


class CategoryReviewView(ListAPIView):
    """
    Fetches reviews filtered by a provided category ID.
    """

    class ReviewSearchPagination(CursorPagination):
        page_size = 5
        ordering = "-id"

    pagination_class = ReviewSearchPagination
    queryset = Metadata.objects
    serializer_class = LatestReviewSerializer

    def filter_queryset(self, queryset):
        """
        Filters the queryset based on a 'category_id' query parameter.

        If category_id is not present, filters all reviews
        """

        category_id = self.request.GET.get("category_id")
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset
