from rest_framework import serializers
from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions, MortgageLoanProducts, MortgageLoanOptions, CreditLoanProducts, CreditLoanOptions


class DepositOptionsSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='DepositOptions.product')
    class Meta:
        model = DepositOptions
        fields = '__all__'


class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'


class SavingOptionsSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='SavingOptions.product')
    class Meta:
        model = SavingOptions
        fields = '__all__'


class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'


class MortgageLoanOptionsSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='MortgageLoanOptions.product')
    class Meta:
        model = MortgageLoanOptions
        fields = '__all__'


class MortgageLoanProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MortgageLoanProducts
        fields = '__all__'


class CreditLoanOptionsSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='CreditLoanOptions.product')
    class Meta:
        model = CreditLoanOptions
        fields = '__all__'


class CreditLoanProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditLoanProducts
        fields = '__all__'