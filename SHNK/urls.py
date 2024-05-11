from django.urls import path
from . import views

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
]
