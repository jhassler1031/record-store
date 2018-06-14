from django.shortcuts import render
from django.db.models import Q

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from record_app.models import Band, Album, Track
from record_app.serializers import BandSerializer, AlbumSerializer, TrackSerializer
from record_app.permissions import IsOwnerOrReadOnly

# Create your views here.

#Band Views
class BandListCreateAPIView(APIView):
    def get(self, request):
        all_bands = Band.objects.all()
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

    #Need search view
class AlbumListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class AlbumRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
