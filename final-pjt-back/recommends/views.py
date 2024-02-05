from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from .models import AddInfo, RealEstate
from .serializers import AddInfoSerializer, ApartSerializer
from accounts.models import Carts
from accounts.serializers import CartsSerializer
from django.db.models import Count
import pandas as pd
from django.db.models import FloatField
from collections import defaultdict
from django.contrib.auth import get_user_model
import locale

# Create your views here.
@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated]) 
def save_info(request):
    # 최초 DB 저장
    if request.method == 'POST':
        save_data = {
            "deposit_money": request.data['depositMoney'],
            "saving_money": request.data['savingMoney'],
            "total_money": request.data['totalMoney'],
            "target_place": request.data['targetPlace'],
            "move_time": request.data['moveTime'],
        }

        existing_data = AddInfo.objects.filter(user=request.user)
        if existing_data.exists():
            serializer = AddInfoSerializer(existing_data.first(), data=save_data)
        else:
            serializer = AddInfoSerializer(data=save_data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return JsonResponse({ 'message': 'okay' })
    
    # DB 수정 페이지 요청 시
    if request.method == 'GET':
        try:
            add_info = AddInfo.objects.get(user=request.user)
            serializer = AddInfoSerializer(add_info)
            return Response(serializer.data)
        except AddInfo.DoesNotExist:
            return Response('first')



@api_view(['GET'])
def view_info(request):
    products = AddInfo.objects.all()
    serializer = AddInfoSerializer(products, many=True)
    return Response(serializer.data)


def save_apart(request):
    excel_file_path = 'sigungu.xlsx'
    df = pd.read_excel(excel_file_path)

    for index, row in df.iterrows():
        RealEstate.objects.create(
            sigu = row['시'],
            average_price = row['23.10 평균매매가격(1000원)']
        )

    return JsonResponse({'message': 'Data saved successfully.'})


@api_view(['GET'])
def apart(request):
    aparts = RealEstate.objects.all().order_by('sigu')
    serializer = ApartSerializer(aparts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recommends_products(request):
    # 아래 2개는 사용자의 데이터
    # 이 데이터들을 가지고 같은 지역의 사람들과 비슷한 돈을 가진 사람들을 뽑아서 보내주기
    user_target_place = request.GET.get('targetPlace')
    apart = RealEstate.objects.get(sigu=user_target_place)
    apart_price = apart.average_price * 1000
    locale.setlocale(locale.LC_ALL, '')
    formatted_price = locale.format_string("%d", apart_price, grouping=True)
    
    user_total_money = float(request.GET.get('totalMoney'))
    user_model = get_user_model()

    lower_bound = user_total_money - (user_total_money * 0.25)
    upper_bound = user_total_money + (user_total_money * 0.25)
    similar_addinfo = AddInfo.objects.exclude(user=request.user).filter(
        target_place=user_target_place,
        total_money__gte=lower_bound,
        total_money__lte=upper_bound
    )
    similar_carts = []
    for item in similar_addinfo:
        similar_cart = Carts.objects.filter(user_id=item.user_id)
        similar_carts.extend(similar_cart)

    product_freq = defaultdict(int)
    # similar_carts에 있는 모든 상품의 빈도를 측정합니다
    for cart in similar_carts:
        product_freq[cart.fin_prdt_cd] += 1

    # 가장 빈도가 높은 상위 10개의 상품을 선택합니다
    top_10_products = sorted(product_freq, key=product_freq.get, reverse=True)[:10]
    print(top_10_products)
    
    cart_list = []
    cart_dict = {'top_10_carts': [], 'user_with_carts': [], 'apt_transaction': formatted_price }
    for product_cd in top_10_products:
        for cart in similar_carts:
            if cart.fin_prdt_cd == product_cd:
                cart_dict['top_10_carts'].append({'fin_prdt_cd': cart.fin_prdt_cd, 'kor_co_nm': cart.kor_co_nm, 'fin_prdt_nm': cart.fin_prdt_nm})
                break
                
                
    # 총 자본과의 차이가 나지 않는 순으로 5명 뽑기
    # 일단은 지역이 같은 것들
    similar_addinfo = AddInfo.objects.exclude(user=request.user).filter(
        target_place=user_target_place,
    )
    
    sorted_similar_addinfo = sorted(similar_addinfo, key=lambda add_info: abs(add_info.total_money - user_total_money))[:5]


    for item in sorted_similar_addinfo:
        similar_cart = Carts.objects.filter(user_id=item.user_id)
        user = user_model.objects.get(id=item.user_id)
        # print(user)
        user_dic = {}
        user_dic['move_time'] = item.move_time
        user_dic['id'] = user.username
        user_dic['gender'] = user.gender
        user_dic['age'] = user.age
        user_dic['nickname'] = user.nickname
        user_dic['total_money'] = item.total_money
        user_dic['user_carts'] = []
        for cart in similar_cart:
            user_dic['user_carts'].append({'fin_prdt_cd': cart.fin_prdt_cd, 'kor_co_nm': cart.kor_co_nm, 'fin_prdt_nm': cart.fin_prdt_nm})
        cart_dict['user_with_carts'].append(user_dic)
        
    cart_list.append(cart_dict)
        
    # print(cart_list)
    return Response(cart_list)


@api_view(['GET'])
def products_ranking(request):
    # 각 fin_prdt_cd의 빈도수를 계산하고 정렬
    products = Carts.objects.values('fin_prdt_cd', 'kor_co_nm', 'fin_prdt_nm').annotate(
        frequency=Count('fin_prdt_cd')).order_by('-frequency')

    # 상위 10개 항목까지 시리얼라이징하여 전달
    serialized_products = []
    for product in products[:10]:
        serialized_product = {
            'fin_prdt_cd': product['fin_prdt_cd'],
            'kor_co_nm': product['kor_co_nm'],
            'fin_prdt_nm': product['fin_prdt_nm'],
            'frequency': product['frequency'],
        }
        serialized_products.append(serialized_product)

    return Response(serialized_products)