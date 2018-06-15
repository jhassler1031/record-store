from django.shortcuts import render
from django.db.models import Q

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend

from record_app.models import Band, Album, Track
from record_app.serializers import BandSerializer, AlbumSerializer, TrackSerializer
from record_app.permissions import IsOwnerOrReadOnly

# Create your views here.

#Band Views=========================================================
class BandListCreateAPIView(APIView):
    def get(self, request):
        all_bands = Band.objects.all()
        query = self.request.query_params.get('band_name', None)
        if query != None:
            all_bands = all_bands.filter(band_name__icontains=query)
        serialized_bands = BandSerializer(all_bands, many=True)
        return Response(serialized_bands.data, 200)

    def post(self, request):
        band_name = request.POST["band_name"]
        genre = request.POST["genre"]
        city_origin = request.POST["city_origin"]
        year_formed = request.POST["year_formed"]
        author = self.request.user

        new_band = Band.objects.create(band_name=band_name, genre=genre, city_origin=city_origin, year_formed=year_formed, author=author)
        serialized_band = BandSerializer(new_band)
        return Response(serialized_band.data, 201)

class BandDetailAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, pk):
        band = Band.objects.get(id=pk)
        serialized_band = BandSerializer(band)
        return Response(serialized_band.data, 200)

    def put(self, request, pk):
        band = Band.objects.get(id=pk)
        self.check_object_permissions(request, band)
        band.band_name = request.POST["band_name"]
        band.genre = request.POST["genre"]
        band.city_origin = request.POST["city_origin"]
        band.year_formed = request.POST["year_formed"]
        band.author = self.request.user
        band.save()
        serialized_band = BandSerializer(band)
        return Response(serialized_band.data, 200)

    def delete(self, request, pk):
        band = Band.objects.get(id=pk)
        self.check_object_permissions(request, band)
        band.delete()
        return Response("", 204)

#Album Views ======================================================
class AlbumListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AlbumSerializer

    def get_queryset(self):
        queryset = Album.objects.all()
        query = self.request.query_params.get('title', None)
        if query != None:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class AlbumRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

#Track Views ========================================================
class TrackListCreateAPIView(APIView):
    def get(self, request):
        all_tracks = Track.objects.all()
        query = self.request.query_params.get('title', None)
        if query != None:
            all_tracks = all_tracks.filter(title__icontains=query)
        serialized_tracks = TrackSerializer(all_tracks, many=True)
        return Response(serialized_tracks.data, 200)

    def post(self, request):
        title = request.POST["title"]
        album_id = request.POST["album"]
        author = self.request.user

        new_track = Track.objects.create(title=title, album_id=album_id, author=author)
        serialized_track = TrackSerializer(new_track)
        return Response(serialized_track.data, 201)

class TrackDetailAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, pk):
        track = Track.objects.get(id=pk)
        serialized_track = TrackSerializer(track)
        return Response(serialized_track.data, 200)

    def put(self, request, pk):
        track = Track.objects.get(id=pk)
        self.check_object_permissions(request, track)
        track.title = request.POST["title"]
        track.album_id = request.POST["album"]
        track.author = self.request.user
        track.save()

        serialized_track = TrackSerializer(track)
        return Response(serialized_track.data, 200)

    def delete(self, request, pk):
        track = Track.objects.get(id=pk)
        self.check_object_permissions(request, track)
        track.delete()
        return Response("", 204)
