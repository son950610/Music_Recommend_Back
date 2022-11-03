from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('<int:song_id>/', views.SongView.as_view(), name='song_view'),
    path('<int:song_id>/song_like/', views.SongLikeView.as_view(), name='song_like_view'),
]