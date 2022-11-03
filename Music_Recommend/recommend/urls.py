from django.urls import path
from recommend import views

urlpatterns = [
    path('songs/', views.SongListView.as_view(), name="song-list"),    
    path('songs/<int:song_id>/', views.SongRecommendView.as_view(), name="song-recommend"),   
]