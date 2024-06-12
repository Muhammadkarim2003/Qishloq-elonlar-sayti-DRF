from django.contrib import admin
from .models import Category, Ads, Comment, Streert, Mahalla


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['description']

class CategoryAdmin(admin.ModelAdmin):
    pass

class AdsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ads)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Mahalla)
admin.site.register(Streert)



