from django.urls import path

from . import views

urlpatterns = [
    #song
    path('<int:song_id>/', views.SongView.as_view(), name='song_view'),
    path('<int:song_id>/song_like/', views.SongLikeView.as_view(), name='song_like_view'),
    path('search/',views.SearchView.as_view(),name='search_view'),

    #voice
    path('<int:song_id>/voice/', views.VoiceView.as_view(), name='voice_view'),
    path('<int:voice_id>/voice_like/', views.VoiceLikeView.as_view(), name='voice_like_view'),
    path('<int:song_id>/voice/<int:voice_id>/', views.VoiceDetailView.as_view(), name='voice_detail_view'),
    
    #comment
    path('<int:song_id>/comment/', views.CommentView.as_view(), name='comment_view'),
    path('<int:song_id>/comment/<int:comment_id>/', views.CommentDetailView.as_view(), name='comment_detail_view'),
]