from rest_framework import serializers

from .models import Playlist
from songs.models import Song
class PlaylistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('title', 'content')
        
class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"

class SongDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("title", "singer", "genre")

class PlaylistDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    playlist_detail = SongDetailSerializer(many=True)
    
    def get_user(self, obj):
        return obj.user.nickname
    class Meta:
        model = Playlist
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'playlist_detail','user',)
        