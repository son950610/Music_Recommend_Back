from django.contrib import admin

from .models import Song, Voice, Comment

admin.site.register(Song)
admin.site.register(Voice)
admin.site.register(Comment)
