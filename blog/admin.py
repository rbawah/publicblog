from django.contrib import admin
from .models import Post, Topic, Geolocation#, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Geolocation)