from .models import ContactInfoModel
from rest_framework import serializers

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfoModel
        fields = "__all__"