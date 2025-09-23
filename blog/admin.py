from django.contrib import admin
from .models import BlogPost, Tag

admin.site.register(BlogPost)
admin.site.register(Tag)
