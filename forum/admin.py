from django.contrib import admin
from .models import Head, Comment
# Register your models here.




class CommentInline(admin.TabularInline):  # new
    model = Comment


class ForumAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Head, ForumAdmin)
admin.site.register(Comment)