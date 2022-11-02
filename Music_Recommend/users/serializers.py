from rest_framework import serializers
from .models import User
from .validators import contains_special_character, contains_uppercase_letter, contains_lowercase_letter, contains_number

class UserSerializer(serializers.ModelSerializer):
    repassword= serializers.CharField(error_messages={'required':'비밀번호를 입력해주세요.', 'blank':'비밀번호를 입력해주세요.'})    
    
    class Meta:
        model = User
        fields = ('email', 'nickname', 'password', 'repassword',)
        extra_kwargs = {'email': {
                        'error_messages': {
                        'required': '이메일을 입력해주세요.',
                        'invalid': '알맞은 형식의 이메일을 입력해주세요.',
                        'blank':'이메일을 입력해주세요.',}},
                        
                        'nickname': {
                        'error_messages': {
                        'required': '닉네임을 입력해주세요.',
                        'blank':'닉네임을 입력해주세요',}},
                        
                        'password':{'write_only':True,
                        'error_messages': {
                        'required':'비밀번호를 입력해주세요.',
                        'blank':'비밀번호를 입력해주세요.',}},
                        } #extra_kwargs에 write_only하여 password만큼은 직렬화 시키지 않겠다.

    def validate(self, data):
        nickname = data.get('nickname')
        password = data.get('password')
        repassword = data.get('repassword')
        
        if contains_special_character(nickname) or len(nickname) < 3:
            raise serializers.ValidationError(detail={"nickname":"닉네임은 2자 이하 또는 특수문자를 포함할 수 없습니다."})
        
        if password != repassword:
            raise serializers.ValidationError(detail={"password":"비밀번호가 일치하지 않습니다."})
        
        if ( len(password) < 8 or len(password) > 17 
            or not contains_uppercase_letter(password)
            or not contains_lowercase_letter(password)
            or not contains_number(password) 
            or not contains_special_character(password) 
            ):
            raise serializers.ValidationError(detail={"password":"비밀번호는 8자 이상 16자이하의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다. "})
        
        return data
    
    def create(self, validated_data):
        email = validated_data['email']
        nickname = validated_data['nickname']
        user= User(
            nickname=nickname,
            email=email
        ) 
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, validated_data):
        email = validated_data['email']
        nickname = validated_data['nickname']
        user = User(email=email, nickname=nickname)
        user.save()
        return user



