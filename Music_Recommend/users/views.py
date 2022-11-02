from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import get_object_or_404
from .jwt_claim_serializer import CustomTokenObtainPairSerializer

from .serializers import UserSerializer
from .models import User

# Create your views here.

class UserView(APIView):
    #회원가입
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입성공"}, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
    #회원정보 수정
    def put(self, request):
        user = get_object_or_404(User, id=request.user.id)
        if user == request.user:
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"회원정보 수정 성공"} , status=status.HTTP_201_CREATED)
            return Response({"message":"회원정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"접근 권한 없음"}, status=status.HTTP_403_FORBIDDEN)

    #회원탈퇴
    def delete(self, request):
        user = get_object_or_404(User, id=request.user.id)
        if user:
            user.delete()
            return Response({"message":"회원탈퇴 성공"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message":"회원탈퇴 실패"}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer