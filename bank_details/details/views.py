from django.shortcuts import render,HttpResponse
import csv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BankDetailsSerializers
from .models import BankDetails
# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'Bank Details By Bank Branch IFSC code':'/BankDetail/<str:pk>/',
        'Bank Details By Bank Name and City': '/AllBrancheDetails/<str:pk1>/<str:pk2>/',
		}

	return Response(api_urls)


@api_view(['GET'])
def BankDetail(request, pk):
	Details = BankDetails.objects.get(ifsc=pk)
	serializer = BankDetailsSerializers(Details, many=False)
	return Response(serializer.data)

@api_view(['GET'])
def AllBrancheDetails(request, pk1,pk2):
	Details = BankDetails.objects.filter(city=pk2).filter(bank_name=pk1)
	serializer = BankDetailsSerializers(Details, many=True)
	return Response(serializer.data)

def data(request):
    with open('C:/Users/SAI KRISHNA/python/projects/Indian_Banks/bank_details/templates/data.csv',
              encoding="utf8") as f:
        reader = csv.reader(f)
        for line in reader:
            product = BankDetails()
            product.ifsc = line[0]
            product.bank_id = line[1]
            product.branch = line[2]
            product.address = line[3]
            product.city = line[4]
            product.district = line[5]
            product.state = line[6]
            product.bank_name = line[7]
            product.save()