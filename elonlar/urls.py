from django.urls import path
from .views import (CategoryCreateView, CategoryListView, CategoryRetriewUpdateDestroyerView,
                    MahallaCreateView, MahallaListView, MahallaRetriewUpdateDestroyerView,
                    StreetCreateApi, StreetListView, StreetRetriewUpdateDestroyerView,
                    AdsCreateView, AdsListView, AdsRetriewUpdateDestroyerView,
                    AdsByCategoryAPIView, MahallaStreetFilterAPIView)


urlpatterns = [
    path('category-created/', CategoryCreateView.as_view()),
    path('category-list/', CategoryListView.as_view()),
    path('category-rud/<uuid:pk>/', CategoryRetriewUpdateDestroyerView.as_view()),

    path('mahalla-create/', MahallaCreateView.as_view()),
    path('mahalla-list/', MahallaListView.as_view()),
    path('mahalla-rud/<uuid:pk>/', MahallaRetriewUpdateDestroyerView.as_view()),

    path('kocha-create/', StreetCreateApi.as_view()),
    path('kocha-list/', StreetListView.as_view()),
    path('kocha-rud/<uuid:pk>/', StreetRetriewUpdateDestroyerView.as_view()),

    path('ads-list/', AdsListView.as_view()),
    path('ads-create/', AdsCreateView.as_view()),
    path('ads-rud/<uuid:pk>/', AdsRetriewUpdateDestroyerView.as_view()),

    path('ads/by-category/<uuid:category_id>/', AdsByCategoryAPIView.as_view()),
    path('mahalla-street-filter/<uuid:mahalla_id>/', MahallaStreetFilterAPIView.as_view()),
]