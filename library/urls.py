from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path("schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("books/", views.ListBook.as_view()),
    path("books/<int:pk>/", views.RetrieveBook.as_view()),
    path("books/relate-book/<int:pk>", views.ListRelateBook.as_view()),
    path("books/most-borrow/", views.ListMostBorrowBook.as_view()),
    path("authors/", views.ListAuthor.as_view()),
    path("genres/", views.ListGenre.as_view()),
    path("publishers/", views.ListPublisher.as_view()),
    path("requests/", views.ListCreateRequest.as_view()),
    path("requests/<int:pk>/", views.DeleteRequest.as_view()),
    path("borrows/", views.ListBorrow.as_view()),
    path("user/", views.RetrieveUser.as_view()),
    path("reviews/books/<int:pk>/", views.ListCreateReviewByBook.as_view())
]
