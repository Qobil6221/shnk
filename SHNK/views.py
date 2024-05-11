from . import serializers
from . import models
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


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

