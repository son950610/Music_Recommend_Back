from rest_framework import serializers
from songs.models import Song, Voice

class SongSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    song_likes = serializers.StringRelatedField(many=True)   

    def get_user(self, obj): 
        return obj.user.email

    class Meta:
        model = Song
        fields = "__all__"

class VoiceSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    voice_likes = serializers.StringRelatedField(many=True)
    song = serializers.StringRelatedField()
    
    def get_user(self, obj): 
        return obj.user.email
    class Meta:
        model = Voice
        fields = "__all__"
        
class VoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voice
        fields = ('recode',)
        
class VoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voice
        fields = '__all__'