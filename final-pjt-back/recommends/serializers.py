from rest_framework import serializers
from .models import AddInfo, RealEstate

class AddInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddInfo
        fields = '__all__'
        read_only_fields = ('user', )


class ApartSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = '__all__'