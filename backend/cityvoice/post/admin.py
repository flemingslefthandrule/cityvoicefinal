from django.contrib import admin
from .models import Post, Label

admin.site.register(Post)
admin.site.register(Label)