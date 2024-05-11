from rest_framework import serializers
from .models import (
    Xabarlar, 
    Elonlar,
    Rahbariyat,
    Tarkibiy_bolinmalar,
    Standartlar
)

class XabarlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xabarlar
        fields = "__all__"
class ElonlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elonlar
        fields = "__all__"
        
class RahbariyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rahbariyat
        fields = "__all__"

class Tarkibiy_bolinmalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarkibiy_bolinmalar
        fields = "__all__"

class StandartlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standartlar
        fields = "__all__"
