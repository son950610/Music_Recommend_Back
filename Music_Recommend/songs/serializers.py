from rest_framework import serializers

from songs.models import Song, Voice, Comment

class SongSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Song
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = "__all__"

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)

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

