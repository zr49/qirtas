from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'status', 'image_preview')
    search_fields = ('title', 'content')
    list_filter = ('date_created', 'author')
    ordering = ('-date_created',)
    def image_preview(self,obj):
        if obj.image:
            return "يوجد صورة"
        return "لا يوجد صورة"
    image_preview.short_description = "الحالة البصرية"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','post','created_date')
    search_feilds = ('author','text')
    list_filter = ('created_date',)