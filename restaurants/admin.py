from django.contrib import admin
from .models import Restaurant, Comment,Reklama


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['title', 'categories', 'user',
                    ]
    search_fields = ['title']
    list_filter = ['user', 'created_at']
    list_per_page = 20
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'created_at']
    search_fields = ['text']
    list_per_page = 20
    date_hierarchy = 'created_at'
admin.site.register(Reklama)