from django.urls import path
from .views import ProfileCreateView, ProfileListView, ProfileRetrieveUpdateDestroyerView

urlpatterns = [
    path('create/', ProfileCreateView.as_view()),
    path('list/', ProfileListView.as_view()),
    path('rud/uuid:pk/', ProfileRetrieveUpdateDestroyerView.as_view()),
]