from django.shortcuts import render
from .serializers import AdsSerializers, CategorySerializers, MahallaSerializers, StreetSerializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, Mahalla, Streert, Ads
from .permission import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly
from rest_framework import filters
from django.contrib.auth.models import User

# Category class
class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategoryRetriewUpdateDestroyerView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers



#Mahalla clasi
class MahallaCreateView(CreateAPIView):
    queryset = Mahalla.objects.all()
    serializer_class = MahallaSerializers

class MahallaListView(ListAPIView):
    queryset = Mahalla.objects.all()
    serializer_class = MahallaSerializers

class MahallaRetriewUpdateDestroyerView(RetrieveUpdateDestroyAPIView):
    queryset = Mahalla.objects.all()
    serializer_class = MahallaSerializers


#Street clasi
class StreetCreateApi(CreateAPIView):
    queryset = Streert.objects.all()
    serializer_class = StreetSerializers

class StreetListView(ListAPIView):
    queryset = Streert.objects.all()
    serializer_class = StreetSerializers

class StreetRetriewUpdateDestroyerView(RetrieveUpdateDestroyAPIView):
    queryset = Streert.objects.all()
    serializer_class = StreetSerializers



#post clasi
class AdsCreateView(CreateAPIView):
    queryset = Ads
    serializer_class = AdsSerializers

class AdsListView(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class AdsRetriewUpdateDestroyerView(RetrieveUpdateDestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializers
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


class AdsByCategoryAPIView(ListAPIView):
    serializer_class = AdsSerializers

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Ads.objects.filter(category_id=category_id)

class MahallaStreetFilterAPIView(ListAPIView):
    serializer_class = MahallaSerializers
    def get_queryset(self):
        mahalla_id = self.kwargs['mahalla_id']
        return Streert.objects.filter(mahalla_id=mahalla_id)

class UserList(ListAPIView):
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Ads.objects.filter(user_id=user_id)

