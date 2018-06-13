from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from record_app.models import Band, Album, Track

#Create serializers here

#Band serializer
class BandSerializer(ModelSerializer):
    albums = serializers.ListField(read_only=True)

    class Meta:
        model = Band
        fields = "__all__"
        read_only_fields = ['author', 'albums']

#Album Serializer
class AlbumSerializer(ModelSerializer):
    tracks = serializers.ListField(read_only=True)

    class Meta:
        model = Album
        fields = "__all__"
        read_only_fields = ['author', 'tracks']

#Track Serializer
class TrackSerializer(ModelSerializer):

    class Meta:
        model = Track
        fields = "__all__"
        read_only_fields = ['author']
