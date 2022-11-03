from rest_framework import serializers
from songs.models import Song

class SongSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes = serializers.StringRelatedField(many=True)   

    def get_user(self, obj): 
        return obj.user.email

    class Meta:
        model = Song
        fields = "__all__"