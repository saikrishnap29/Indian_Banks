from django.db import models

# Create your models here.

class BankDetails(models.Model):
    ifsc=models.CharField(max_length=20,primary_key=True)
    bank_id=models.IntegerField()
    branch= models.CharField(max_length=80)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=30)
    bank_name=models.CharField(max_length=100)
