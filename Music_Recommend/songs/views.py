from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Song, Voice
from songs.serializers import SongSerializer, VoiceCreateSerializer, VoiceSerializer, VoiceDetailSerializer
# Create your views here.


class SongView(APIView):
    def get(self, request, song_id):
        song = get_object_or_404(Song, id=song_id)
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SongLikeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, song_id):
        song = get_object_or_404(Song, id=song_id)
        if request.user in song.song_likes.all():
            song.song_likes.remove(request.user)
            return Response("좋아요 취소했습니다.", status=status.HTTP_204_NO_CONTENT)
        else:
            song.song_likes.add(request.user)
            return Response("좋아요 했습니다.", status=status.HTTP_200_OK)

class SearchView(APIView):
    def get(self, request):
        post_result = Song.object.all()
    pass

class VoiceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, song_id):
        song = get_object_or_404(Song, id=song_id)
        voice = song.voice_set.all()
        serializer = VoiceSerializer(voice, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, song_id):
        serializer = VoiceCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, song_id=song_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VoiceDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, song_id, voice_id):
        voice = get_object_or_404(Voice, id=voice_id)
        serializer = VoiceDetailSerializer(voice)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, song_id, voice_id):
        voice = get_object_or_404(Voice, id=voice_id)
        if request.user == voice.user:
            serializer = VoiceCreateSerializer(voice, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, song_id=song_id)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, song_id, voice_id):
        voice = get_object_or_404(Voice, id=voice_id)
        if request.user == voice.user:
            voice.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
        
class VoiceLikeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, voice_id):
        voice = get_object_or_404(Voice, id=voice_id)
        if request.user in voice.voice_likes.all():
            voice.voice_likes.remove(request.user)
            return Response("좋아요 취소했습니다.", status=status.HTTP_200_OK)
        else:
            voice.voice_likes.add(request.user)
            return Response("좋아요 했습니다.", status=status.HTTP_200_OK)