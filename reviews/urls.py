from django.urls import path

from reviews import views

app_name = "reviews"

urlpatterns = [
    path("trends", views.ReviewTrendView.as_view()),
    path("", views.CategoryReviewView.as_view()),
]
