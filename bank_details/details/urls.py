from django.urls import path
from.import views

urlpatterns=[
    path('', views.ApiOverview, name="ApiOverview"),
	path('BankDetail/<str:pk>/', views.BankDetail, name="BankDetail"),
    path('AllBrancheDetails/<str:pk1>/<str:pk2>/', views.AllBrancheDetails, name="AllBrancheDetails"),
    path('data/',views.data,name='data')
]