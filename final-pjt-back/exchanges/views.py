from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import requests
from .models import Exchanges
from .serializers import ExchangesSerializer
from django.conf import settings

API_KEY = settings.EXCHANGE_KEY
print(API_KEY)

# Create your views here.
@api_view(['GET'])
def save_exchange_data(request):
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&data=AP01'
    exchanges = requests.get(url).json()
    print(exchanges)
    for li in exchanges:
        cur_unit = li.get("cur_unit")
        try:
            exchange = Exchanges.objects.get(cur_unit=cur_unit)
            exchange.ttb = li.get("ttb")
            exchange.tts = li.get("tts")
            exchange.deal_bas_r = li.get("deal_bas_r")
            exchange.bkpr = li.get("bkpr")
            exchange.yy_efee_r = li.get("yy_efee_r")
            exchange.ten_dd_efee_r = li.get("ten_dd_efee_r")
            exchange.kftc_bkpr = li.get("kftc_bkpr")
            exchange.kftc_deal_bas_r = li.get("kftc_deal_bas_r")
            exchange.cur_nm = li.get("cur_nm")
            exchange.save()

        except Exchanges.DoesNotExist:                
            save_data = {
                "cur_unit": li.get("cur_unit"),
                "ttb": li.get("ttb"),
                "tts": li.get("tts"),
                "deal_bas_r": li.get("deal_bas_r"),
                "ten_dd_efee_r": li.get("ten_dd_efee_r"),
                "mtrt_int": li.get("mtrt_int"),
                "kftc_bkpr": li.get("kftc_bkpr"),
                "yy_efee_r": li.get("yy_efee_r"),
                "bkpr": li.get("bkpr"),
                "kftc_deal_bas_r": li.get("kftc_deal_bas_r"),
                "cur_nm": li.get("cur_nm"),
            }

            serializer = ExchangesSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    return JsonResponse({ 'message': 'okay' })


@api_view(['GET'])
def pull_exchanges(request):
    products = Exchanges.objects.all()
    serializer = ExchangesSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def pull_list(request):
    units = Exchanges.objects.values_list('cur_unit', flat=True)
    names = Exchanges.objects.values_list('cur_nm', flat=True)
    exchanges = []
    for name, unit in zip(names, units):
        exchanges.append(f'{name} [{unit}]')

    return Response(exchanges)