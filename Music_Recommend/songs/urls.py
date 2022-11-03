from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('<int:song_id>/', views.SongView.as_view(), name='song_view'),
    path('<int:song_id>/song_like/', views.SongLikeView.as_view(), name='song_like_view'),
    path('<int:song_id>/voice/', views.VoiceView.as_view(), name='voice_view'),
    path('<int:voice_id>/voice_like/', views.VoiceLikeView.as_view(), name='voice_like_view'),
    path('<int:song_id>/voice/<int:voice_id>/', views.VoiceDetailView.as_view(), name='voice_detail_view'),
]