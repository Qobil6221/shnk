from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'systems',  views.SHNKSystemsViewSet, basename='system')
router.register(r'groups',  views.SHNKGroupsViewSet, basename='group')
router.register(r'types', views.SHNKTypesViewSet, basename='type')
router.register(r'documents',  views.SHNKDocumentsViewSet, basename='documents')

urlpatterns = router.urls

urlpatterns = [
    path('xabarlar/', views.XabarlarAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('xabarlar/<int:pk>/', views.XabarlarAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('elonlar/', views.ElonlarAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('elonlar/<int:pk>/', views.ElonlarAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('rahbariyat/', views.RahbariyatAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('rahbariyat/<int:pk>/', views.RahbariyatAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('standartlar/', views.StandartlarAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('standartlar/<int:pk>/', views.StandartlarAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('tarkibiy/', views.Tarkibiy_bolinmalarAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('tarkibiy/<int:pk>/', views.Tarkibiy_bolinmalarAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),    
    path('boglanish/', views.BoglanishAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('boglanish/<int:pk>/', views.BoglanishAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),    
    path('qurilish_regmentlari/', views.QRAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('qurilish_regmentlari/<int:pk>/', views.QRAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),    
    path('esf/', views.ESFAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('esf/<int:pk>/', views.ESFAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),    
    path('lugat/', views.LugatAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('lugat/<int:pk>/', views.LugatAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),    
]
