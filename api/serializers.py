# api/serializers.py
from rest_framework import serializers
from .models import Enqueteur, Enquete

class EnqueteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enqueteur
        fields = '__all__'

class EnqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquete
        fields = '__all__'
