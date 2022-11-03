from rest_framework import serializers
from .models import Playlist

class PlaylistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('title', 'content')
        
class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"
        
class PlaylistDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Playlist
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'playlist_detail','user',)