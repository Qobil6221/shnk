from . import serializers
from . import models
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter



class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class XabarlarAPIView(viewsets.ModelViewSet):
    queryset = models.Xabarlar
    serializer_class = serializers.XabarlarSerializer
    pagination_class = LargeResultsSetPagination

class ElonlarAPIView(viewsets.ModelViewSet):
    queryset = models.Elonlar
    serializer_class = serializers.ElonlarSerializer
    pagination_class = LargeResultsSetPagination

class RahbariyatAPIView(viewsets.ModelViewSet):
    queryset = models.Rahbariyat
    serializer_class = serializers.RahbariyatSerializer

class StandartlarAPIView(viewsets.ModelViewSet):
    queryset = models.Standartlar
    serializer_class = serializers.StandartlarSerializer

class Tarkibiy_bolinmalarAPIView(viewsets.ModelViewSet):
    queryset = models.Tarkibiy_bolinmalar
    serializer_class = serializers.Tarkibiy_bolinmalarSerializer

class BoglanishAPIView(viewsets.ModelViewSet):
    queryset = models.Boglanish
    serializer_class = serializers.BoglanishSerializer

class QRAPIView(viewsets.ModelViewSet):
    queryset = models.Qurilish_reglamentlari
    serializer_class = serializers.QRSerializer

class ESFAPIView(viewsets.ModelViewSet):
    queryset = models.ESF
    serializer_class = serializers.ESFSerializer

class LugatAPIView(viewsets.ModelViewSet):
    queryset = models.Lugat
    serializer_class = serializers.LugatSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (SearchFilter,)

    def get_queryset(self): #urlsga startwith/ deb harflar bo'yicha filtirlaydi
        startswith = self.request.GET.get('filter', '')
        return models.Lugat.objects.filter(name__startswith=startswith)
    
class SHNKSystemsViewSet(viewsets.ModelViewSet):
    queryset = models.SHNKSystemsModel

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.SHNKSystemsGETSerializer
        return serializers.SHNKSystemsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save


class SHNKGroupsViewSet(viewsets.ModelViewSet):
    queryset = models.SHNKGroupsModel

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.SHNKGroupsGETSerializer
        return serializers.SHNKGroupsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save


class SHNKTypesViewSet(viewsets.ModelViewSet):
    queryset =models. SHNKTypesModel
    serializer_class = serializers.SHNKTypesSerializer


class SHNKDocumentsViewSet(viewsets.ModelViewSet):
    queryset = models.SHNKDocumentsModel

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.SHNKDocGETSerializer
        return serializers.SHNKDocSerializer