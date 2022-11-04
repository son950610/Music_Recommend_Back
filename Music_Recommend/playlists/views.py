from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Playlist
from songs.models import Song
from .serializers import PlaylistCreateSerializer, PlaylistSerializer, PlaylistDetailSerializer

class PlaylistView(APIView):
    permission_classes = [IsAuthenticated]
    
    #플레이리스트 전체 리스트
    def get(self, request):
        playlist = Playlist.objects.filter(user=request.user.id)
        serializer = PlaylistSerializer(playlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #플레이리스트 생성
    def post(self, request):
        serializer = PlaylistCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaylistDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    #플레이리스트에 노래 여러 개 추가
    def post(self, request, playlist_id):
        song_list = list(request.data["id"])
        playlist_detail = get_object_or_404(Playlist, id=playlist_id).playlist_detail
        for i in range(len(song_list)):
            song = Song.objects.get(id=song_list[i])
            if playlist_detail.filter(id=song_list[i]).exists():
                return Response({"message":f"'{song.singer}의 {song.title}'(이)가 플레이리스트에 이미 추가되어있음"}, status=status.HTTP_201_CREATED)
            playlist_detail.add(song)
        return Response({"message":"플레이리스트에 노래 추가 "}, status=status.HTTP_201_CREATED)
    
    #플레이리스트 상세페이지
    def get(self, request, playlist_id):
        playlist = get_object_or_404(Playlist, id=playlist_id )
        serializer = PlaylistDetailSerializer(playlist)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    #플레이리스트 수정
    def put(self, request, playlist_id):
        playlist = get_object_or_404(Playlist, id=playlist_id )
        if request.user == playlist.user:
            serializer = PlaylistCreateSerializer(playlist, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data , status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("접근 권한 없음", status=status.HTTP_403_FORBIDDEN)
    
    #플레이리스트 삭제
    def delete(self, request, playlist_id):
        playlist = get_object_or_404(Playlist, id=playlist_id )
        if request.user == playlist.user:
            playlist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("접근 권한 없음", status=status.HTTP_403_FORBIDDEN)