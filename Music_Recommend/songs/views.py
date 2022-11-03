from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from .models import Song
from songs.serializers import SongSerializer
# Create your views here.


class SongView(APIView):
    def get(self, request, song_id):
        song = get_object_or_404(Song, id=song_id)
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class SearchView(APIView):
    def get(self, request):
        post_result = Song.object.all()
    pass
