from rest_framework import serializers
from .models import Ads, Category, Comment, Mahalla, Streert
from django.contrib.auth.models import User



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class  AdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"





class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class MahallaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahalla
        fields = "__all__"
    

class StreetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Streert
        fields = "__all__"

