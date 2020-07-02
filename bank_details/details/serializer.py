from rest_framework import serializers
from.models import *

class BankDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields = "__all__"