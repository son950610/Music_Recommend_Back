from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/<int:playlist_id>/', views.PlaylistView.as_view(), name='playlist_view'),
    path('<int:user_id>/<int:playlist_id>/<int:song_id>/', views.PlaylistDetailView.as_view(), name='playlist_detail_view'),
]
