from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import requests
from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions, MortgageLoanProducts, MortgageLoanOptions, CreditLoanProducts, CreditLoanOptions
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingProductsSerializer, SavingOptionsSerializer, MortgageLoanProductsSerializer, MortgageLoanOptionsSerializer, CreditLoanProductsSerializer, CreditLoanOptionsSerializer
from django.conf import settings

api_key = settings.PRODUCTS_KEY

# # permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    # DepositProductsSerializer
    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get("fin_prdt_cd")
        try:
            product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            product.kor_co_nm = li.get("kor_co_nm")
            product.fin_prdt_nm = li.get("fin_prdt_nm")
            product.etc_note = li.get("etc_note")
            product.join_deny = li.get("join_deny")
            product.join_member = li.get("join_member")
            product.join_way = li.get("join_way")
            product.spcl_cnd = li.get("spcl_cnd")
            product.save()

        except DepositProducts.DoesNotExist:                
            save_data = {
                "fin_prdt_cd": li.get("fin_prdt_cd"),
                "kor_co_nm": li.get("kor_co_nm"),
                "fin_prdt_nm": li.get("fin_prdt_nm"),
                "etc_note": li.get("etc_note"),
                "join_way": li.get("join_way"),
                "mtrt_int": li.get("mtrt_int"),
                "spcl_cnd": li.get("spcl_cnd"),
                "join_member": li.get("join_member"),
                "join_deny": li.get("join_deny")
            }

            serializer = DepositProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    
    # DepositOptionsSerializer
    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get("fin_prdt_cd")
        try:   
            product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
        except DepositProducts.DoesNotExist:
            continue

        # 예외 처리 1
        if li.get("intr_rate") is None:
            intr_rate = -1
        else:
            intr_rate = li.get("intr_rate")
            
        save_data = {
            "fin_prdt_cd": fin_prdt_cd,
            "intr_rate_type_nm": li.get("intr_rate_type_nm"),
            "save_trm": li.get("save_trm"),
            "intr_rate": intr_rate,
            "intr_rate2": li.get("intr_rate2"),
        }
        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)

    return JsonResponse({ 'message': 'okay' })


@api_view(['GET'])
def deposit_products(request):
    products = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    options = product.depositoptions_set.all()
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def save_saving_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    # SavingProductsSerializer
    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get("fin_prdt_cd")
        try:
            product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            product.kor_co_nm = li.get("kor_co_nm")
            product.fin_prdt_nm = li.get("fin_prdt_nm")
            product.etc_note = li.get("etc_note")
            product.join_deny = li.get("join_deny")
            product.join_member = li.get("join_member")
            product.join_way = li.get("join_way")
            product.spcl_cnd = li.get("spcl_cnd")
            product.save()

        except SavingProducts.DoesNotExist:                
            save_data = {
                "fin_prdt_cd": li.get("fin_prdt_cd"),
                "kor_co_nm": li.get("kor_co_nm"),
                "fin_prdt_nm": li.get("fin_prdt_nm"),
                "etc_note": li.get("etc_note"),
                "join_way": li.get("join_way"),
                "mtrt_int": li.get("mtrt_int"),
                "spcl_cnd": li.get("spcl_cnd"),
                "join_member": li.get("join_member"),
                "join_deny": li.get("join_deny")
            }

            serializer = SavingProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    
    # SavingOptionsSerializer
    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get("fin_prdt_cd")
        try:   
            product = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)
        except SavingProducts.DoesNotExist:
            continue

        # 예외 처리 1
        if li.get("intr_rate") is None:
            intr_rate = -1
        else:
            intr_rate = li.get("intr_rate")
        if li.get("intr_rate2") is None:
            intr_rate2 = -1
        else:
            intr_rate2 = li.get("intr_rate2")
        save_data = {
            "fin_prdt_cd": fin_prdt_cd,
            "intr_rate_type_nm": li.get("intr_rate_type_nm"),
            "save_trm": li.get("save_trm"),
            "intr_rate": intr_rate,
            "intr_rate2": intr_rate2,
        }
        serializer = SavingOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)

    return JsonResponse({ 'message': 'okay' })


@api_view(['GET'])
def saving_products(request):
    products = SavingProducts.objects.all()
    serializer = SavingProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def saving_product_options(request, fin_prdt_cd):
    product = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)
    options = product.savingoptions_set.all()
    serializer = SavingOptionsSerializer(options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def save_mortgageloan_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json?auth={api_key}&topFinGrpNo=050000&pageNo=1'
    response = requests.get(url).json()
    
    # MortgageLoanProductsSerializer
    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get("fin_prdt_cd")
        try:
            product = MortgageLoanProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            product.kor_co_nm = li.get("kor_co_nm")
            product.fin_prdt_nm = li.get("fin_prdt_nm")
            product.loan_inci_expn = li.get("loan_inci_expn")
            product.erly_rpay_fee = li.get("erly_rpay_fee")
            product.dly_rate = li.get("dly_rate")
            product.loan_lmt = li.get("loan_lmt")
            product.join_way = li.get("join_way")
            product.save()

        except MortgageLoanProducts.DoesNotExist:                
            save_data = {
                "fin_prdt_cd": li.get("fin_prdt_cd"),
                "kor_co_nm": li.get("kor_co_nm"),
                "fin_prdt_nm": li.get("fin_prdt_nm"),
                "loan_inci_expn": li.get("loan_inci_expn"),
                "erly_rpay_fee": li.get("erly_rpay_fee"),
                "dly_rate": li.get("dly_rate"),
                "loan_lmt": li.get("loan_lmt"),
                "join_way": li.get("join_way"),
            }

            serializer = MortgageLoanProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    
    # MortgageLoanProductsOptionsSerializer
    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get("fin_prdt_cd")
        try:   
            product = get_object_or_404(MortgageLoanProducts, fin_prdt_cd=fin_prdt_cd)
        except MortgageLoanProducts.DoesNotExist:
            continue

        # # 예외 처리 1
        if li.get("lend_rate_avg") is None:
            lend_rate_avg = -1
        else:
            lend_rate_avg = li.get("lend_rate_avg")
            
        save_data = {
            "fin_prdt_cd": fin_prdt_cd,
            "mrtg_type_nm": li.get("mrtg_type_nm"),
            "rpay_type_nm": li.get("rpay_type_nm"),
            "lend_rate_type_nm": li.get("lend_rate_type_nm"),
            "lend_rate_min": li.get("lend_rate_min"),
            "lend_rate_max": li.get("lend_rate_max"),
            "lend_rate_avg": lend_rate_avg,
        }
        serializer = MortgageLoanOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)

    return JsonResponse({ 'message': 'okay' })


@api_view(['GET'])
def mortgageloan_products(request):
    products = MortgageLoanProducts.objects.all()
    serializer = MortgageLoanProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def mortgageloan_product_options(request, fin_prdt_cd):
    product = get_object_or_404(MortgageLoanProducts, fin_prdt_cd=fin_prdt_cd)
    options = product.mortgageloanoptions_set.all()
    serializer = MortgageLoanOptionsSerializer(options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def save_creditloan_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={api_key}&topFinGrpNo=050000&pageNo=1'
    response = requests.get(url).json()
    
    # CreditLoanProductsSerializer
    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get("fin_prdt_cd")
        try:
            product = CreditLoanProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            product.kor_co_nm = li.get("kor_co_nm")
            product.fin_prdt_nm = li.get("fin_prdt_nm")
            product.crdt_prdt_type_nm = li.get("crdt_prdt_type_nm")
            product.join_way = li.get("join_way")
            product.save()

        except CreditLoanProducts.DoesNotExist:                
            save_data = {
                "fin_prdt_cd": li.get("fin_prdt_cd"),
                "kor_co_nm": li.get("kor_co_nm"),
                "fin_prdt_nm": li.get("fin_prdt_nm"),
                "crdt_prdt_type_nm": li.get("crdt_prdt_type_nm"),
                "join_way": li.get("join_way"),
            }

            serializer = CreditLoanProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    
    # CreditLoanProductsOptionsSerializer
    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get("fin_prdt_cd")
        try:   
            product = get_object_or_404(CreditLoanProducts, fin_prdt_cd=fin_prdt_cd)
        except CreditLoanProducts.DoesNotExist:
            continue

        # # 예외 처리
        if li.get("crdt_grad_4") is None:
            crdt_grad_4 = -1
        else:
            crdt_grad_4 = li.get("crdt_grad_4")
        if li.get("crdt_grad_5") is None:
            crdt_grad_5 = -1
        else:
            crdt_grad_5 = li.get("crdt_grad_5")
        if li.get("crdt_grad_6") is None:
            crdt_grad_6 = -1
        else:
            crdt_grad_6 = li.get("crdt_grad_6")
        if li.get("crdt_grad_10") is None:
            crdt_grad_10 = -1
        else:
            crdt_grad_10 = li.get("crdt_grad_10")                    
        if li.get("crdt_grad_11") is None:
            crdt_grad_11 = -1
        else:
            crdt_grad_11 = li.get("crdt_grad_11")            
        if li.get("crdt_grad_12") is None:
            crdt_grad_12 = -1
        else:
            crdt_grad_12 = li.get("crdt_grad_12")
        if li.get("crdt_grad_13") is None:
            crdt_grad_13 = -1
        else:
            crdt_grad_13 = li.get("crdt_grad_13")

        save_data = {
        "fin_prdt_cd": fin_prdt_cd,
        "crdt_lend_rate_type_nm": li.get("crdt_lend_rate_type_nm"),
        "crdt_grad_1": li.get("crdt_grad_1"),
        "crdt_grad_4": crdt_grad_4,
        "crdt_grad_5": crdt_grad_5,
        "crdt_grad_6": crdt_grad_6,
        "crdt_grad_10": crdt_grad_10,
        "crdt_grad_11": crdt_grad_11,
        "crdt_grad_12": crdt_grad_12,
        "crdt_grad_13": crdt_grad_13,
        "crdt_grad_avg": li.get("crdt_grad_avg"),
    }
        serializer = CreditLoanOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)

    return JsonResponse({ 'message': 'okay' })


@api_view(['GET'])
def creditloan_products(request):
    products = CreditLoanProducts.objects.all()
    serializer = CreditLoanProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def creditloan_product_options(request, fin_prdt_cd):
    product = get_object_or_404(CreditLoanProducts, fin_prdt_cd=fin_prdt_cd)
    options = product.creditloanoptions_set.all()
    serializer = CreditLoanOptionsSerializer(options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def bank_list(request):
    banks = DepositProducts.objects.values_list('kor_co_nm', flat=True).order_by('kor_co_nm').distinct()
    serialized_banks = list(banks)
    return Response(serialized_banks)


@api_view(['GET'])
def corper_list(request):
    corpers = MortgageLoanProducts.objects.values_list('kor_co_nm', flat=True).order_by('kor_co_nm').distinct()
    serialized_corpers = list(corpers)
    return Response(serialized_corpers)