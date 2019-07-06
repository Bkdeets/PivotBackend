from rest_framework import serializers
from .models import Session, Spot, WaveData, Liked, Comment
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password' : {
                'write_only': True,
                'required':True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = '__all__'

class WaveDataSerializer(serializers.ModelSerializer):
    spot = SpotSerializer(many=False)
    class Meta:
        model = WaveData
        fields = '__all__'

class WaveDataCreateUpdateSerializer(serializers.ModelSerializer):
    spot = serializers.PrimaryKeyRelatedField(queryset=Spot.objects.all())
    class Meta:
        model = WaveData
        fields = '__all__'

class LikedSerializer(serializers.ModelSerializer):
    liker = UserSerializer(many=False)
    class Meta:
        model = Liked
        fields = '__all__'

class LikedCreateUpdateSerializer(serializers.ModelSerializer):
    liker = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Liked
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    spot = SpotSerializer(many=False)
    wavedata = WaveDataSerializer(many=False)
    user = UserSerializer(many=False)
    likers = LikedSerializer(many=True)
    comments = CommentSerializer(many=True)
    likes = serializers.SerializerMethodField()

    def get_likes(self, session):
        return len(Liked.objects.filter(session=session.id))

    class Meta:
        model = Session
        fields = '__all__'

class SessionCreateUpdateSerializer(serializers.ModelSerializer):
    spot = serializers.PrimaryKeyRelatedField(queryset=Spot.objects.all())
    wavedata = serializers.PrimaryKeyRelatedField(queryset=WaveData.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Session
        fields = '__all__'
