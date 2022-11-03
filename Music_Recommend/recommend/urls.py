from django.urls import path

from . import views

urlpatterns = [
    path('songs/', views.SongListView.as_view(), name="song-list"),    
    path('songs/<int:song_id>/recommend/', views.SongRecommendView.as_view(), name="song-recommend"),   
]