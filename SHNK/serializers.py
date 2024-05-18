from rest_framework.serializers import SerializerMethodField, ModelSerializer
from .models import (
    Xabarlar, 
    Elonlar,
    Rahbariyat,
    Tarkibiy_bolinmalar,
    Standartlar,
    Boglanish,
    Qurilish_reglamentlari,
    ESF,
    Lugat,
    SHNKSystemsModel,
    SHNKGroupsModel,
    SHNKTypesModel, SHNKDocumentsModel,

)

class XabarlarSerializer(ModelSerializer):
    class Meta:
        model = Xabarlar
        fields = "__all__"
class ElonlarSerializer(ModelSerializer):
    class Meta:
        model = Elonlar
        fields = "__all__"
        
class RahbariyatSerializer(ModelSerializer):
    class Meta:
        model = Rahbariyat
        fields = "__all__"

class Tarkibiy_bolinmalarSerializer(ModelSerializer):
    class Meta:
        model = Tarkibiy_bolinmalar
        fields = "__all__"

class StandartlarSerializer(ModelSerializer):
    class Meta:
        model = Standartlar
        fields = "__all__"

class BoglanishSerializer(ModelSerializer):
    class Meta:
        model = Boglanish
        fields = ("id", "name")

        def get_distinct_data(self):
            queryset = Rahbariyat.objects.values('id', 'name').distinct()
            return queryset

class QRSerializer(ModelSerializer):
    class Meta:
        model = Qurilish_reglamentlari
        fields = "__all__"

class ESFSerializer(ModelSerializer):
    class Meta:
        model = ESF                
        fields = "__all__"

class LugatSerializer(ModelSerializer):

    class Meta:
        model = Lugat
        fields = "__all__"

class SHNKSystemsSerializer(ModelSerializer):
    class Meta:
        model = SHNKSystemsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class SHNKSystemsGETSerializer(ModelSerializer):
    system_name = SerializerMethodField(method_name='get_system_name', read_only=True)

    class Meta:
        model = SHNKSystemsModel
        fields = ('id', 'code', 'system_name')

    def get_system_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.system_name_ru
            return obj.system_name_uz
        except:
            return obj.system_name_uz


class SHNKGroupsSerializer(ModelSerializer):
    class Meta:
        model = SHNKGroupsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class SHNKGroupsGETSerializer(ModelSerializer):
    group_name = SerializerMethodField(method_name='get_group_name', read_only=True)

    class Meta:
        model = SHNKGroupsModel
        fields = ('id', 'group_code', 'group_name')

    def get_group_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.group_name_ru
            return obj.group_name_uz
        except:
            return obj.group_name_uz


class SHNKTypesSerializer(ModelSerializer):
    class Meta:
        model = SHNKTypesModel
        fields = '__all__'


class SHNKDocGETSerializer(ModelSerializer):
    shnk_name = SerializerMethodField(method_name='get_shnk_name', read_only=True)
    shnk_average_rating = SerializerMethodField(method_name='get_shnk_average_rating', read_only=True)

    class Meta:
        model = SHNKDocumentsModel
        fields = ('id', 'shnk_code', 'shnk_name', 'shnk_average_rating')

    def get_shnk_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.shnk_name_ru
            return obj.shnk_name_uz
        except:
            return obj.shnk_name_uz

    def get_shnk_average_rating(self, obj):
        return obj.average_rating()


class SHNKDocSerializer(ModelSerializer):
    class Meta:
        model = SHNKDocumentsModel
        fields = '__all__'
