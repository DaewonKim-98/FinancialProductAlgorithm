# -*- coding: utf-8 -*-
# make_data.py 파일은 랜덤한 더미 데이터를 만드는 예시 파일입니다.
# 반드시, 사용하는 필드를 확인한 후 본인의 프로젝트에 맞게 수정하여 진행해야 합니다.

# [참고] 현재 코드는 아래 User 모델을 기준으로 작성되어 있습니다.
# class User(AbstractBaseUser):
#     username = models.CharField(max_length=30, unique=True)
#     nickname = models.CharField(max_length=255, blank=True, null=True)
#     email = models.EmailField(max_length=254, blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     money = models.IntegerField(blank=True, null=True)
#     salary = models.IntegerField(blank=True, null=True)
#     # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함
#     financial_products = models.TextField(blank=True, null=True)
    
#     # superuser fields
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)


import random
import requests

first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "민서예지도하주윤채현지"
last_name_samples = "준윤우원호후서연아은진"


def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result

dict_keys = ['username', 'gender', 'age', 'nickname', 'password', 'fin_prdt_cd', 'kor_co_nm', 'fin_prdt_nm', 'created_at']

# json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()

nickname_list = []
N = 1000
i = 0

while i < N:
    rn = random_name()
    if rn in nickname_list:
        continue
    
    nickname_list.append(rn)
    i += 1

    
# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = 'accounts/fixtures/accounts.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    j = 0
    for i in range(N):
        # 랜덤한 데이터를 삽입
        file["model"] = "accounts.User"
        file["pk"] = i+1
        file["fields"] = {
            'nickname': nickname_list[i],  # 유저 이름 랜덤 생성
            'age': str(random.randint(1900, 2023)) + '-' + str(random.randint(10, 13)) + '-' + str(random.randint(10, 32)),  # 나이
            'password': "1234",
            'username': 'test' + str(i+1),
            'gender': random.choice(['남성', '여성']),
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        f.write(',')
        
        random_list = [random.choice([{'fin_prdt_cd': 'WR0001B', 'kor_co_nm': '우리은행', 'fin_prdt_nm': 'WON플러스예금'}, {'fin_prdt_cd': '00320342', 'kor_co_nm': '한국스탠다드차타드은행', 'fin_prdt_nm': 'e-그린세이브예금'}, {'fin_prdt_cd': '10511008000996000', 'kor_co_nm': '대구은행', 'fin_prdt_nm': 'DGB주거래우대예금(첫만남고객형)'}, {'fin_prdt_cd': '10511008001004000', 'kor_co_nm': '대구은행', 'fin_prdt_nm': 'DGB행복파트너예금(일반 형)'}, {'fin_prdt_cd': '10511008001166004', 'kor_co_nm': '대구은행', 'fin_prdt_nm': 'DGB함께예금'}, {'fin_prdt_cd': '10511008001278000', 'kor_co_nm': '대구은행', 'fin_prdt_nm': 'IM스마트예금'}, {'fin_prdt_cd': '01030500510002', 'kor_co_nm': '부산은행', 'fin_prdt_nm': 'LIVE정기예금'}, {'fin_prdt_cd': '01030500560002', 'kor_co_nm': '부산은행', 'fin_prdt_nm': '더(The) 특판 정기예금'}, {'fin_prdt_cd': '01030500600002', 'kor_co_nm': '부산은행', 'fin_prdt_nm': '더(The) 레벨업 정기예금'}, {'fin_prdt_cd': 'TD11300027000', 'kor_co_nm': '광주 은행', 'fin_prdt_nm': '미즈월복리정기예금'}, {'fin_prdt_cd': 'TD11300031000', 'kor_co_nm': '광주은행', 'fin_prdt_nm': '스마트모아Dream 정기예금'}, {'fin_prdt_cd': 'TD11300035000', 'kor_co_nm': '광주은행', 'fin_prdt_nm': '굿스타트예금'}, {'fin_prdt_cd': 'TD11300036000', 'kor_co_nm': '광주은행', 'fin_prdt_nm': 'The플러스예금'}, {'fin_prdt_cd': '200000301', 'kor_co_nm': '제주은 행', 'fin_prdt_nm': '제주Dream\n정기예금\n(개인/만기\n지급식)'}, {'fin_prdt_cd': '200000303', 'kor_co_nm': '제주은행', 'fin_prdt_nm': 'J정기예금\n(만기지급식)'}, {'fin_prdt_cd': '10-01-20-024-0046-0000', 'kor_co_nm': '전북은행', 'fin_prdt_nm': 'JB 다이렉트예금통장\n(만 기일시지급식)'}, {'fin_prdt_cd': '10-01-20-024-0059-0000', 'kor_co_nm': '전북은행', 'fin_prdt_nm': 'JB 123  정기예금\n (만기일시지급식)'}, {'fin_prdt_cd': '21001115', 'kor_co_nm': '경남은행', 'fin_prdt_nm': 'BNK더조 은정기예금'}, {'fin_prdt_cd': '21001203', 'kor_co_nm': '경남은행', 'fin_prdt_nm': 'BNK주거래우대정기예금'}, {'fin_prdt_cd': '01211310121', 'kor_co_nm': '중소기업 은행', 'fin_prdt_nm': 'IBK 평생한가족통장(실세금리정기예금)'}, {'fin_prdt_cd': '01211310127', 'kor_co_nm': '중소기업은행', 'fin_prdt_nm': 'i-ONE놀이터예금'}, {'fin_prdt_cd': '01211310130', 'kor_co_nm': '중소기업은행', 'fin_prdt_nm': '1석7조통장(정기예금)'}, {'fin_prdt_cd': '05100', 'kor_co_nm': '한국산업은행', 'fin_prdt_nm': '정기예금'}, {'fin_prdt_cd': '06492', 'kor_co_nm': '한국산업은행', 'fin_prdt_nm': 'KDB 정기예금'}, {'fin_prdt_cd': '010300100335', 'kor_co_nm': '국민은행', 'fin_prdt_nm': 'KB Star 정기 예금'}, {'fin_prdt_cd': '200-0135-12', 'kor_co_nm': ' 신한은행', 'fin_prdt_nm': '쏠편한 정기예금'}, {'fin_prdt_cd': '10-003-1225-0001', 'kor_co_nm': '농협은행주식회사', 'fin_prdt_nm': 'NH왈츠회전예금 II'}, {'fin_prdt_cd': '10-003-1381-0001', 'kor_co_nm': '농협은행주식회사', 'fin_prdt_nm': 'NH내가Green초록세상예금'}, {'fin_prdt_cd': '10-003-1384-0001', 'kor_co_nm': '농협은행주식회사', 'fin_prdt_nm': 'NH올원e예금'}, {'fin_prdt_cd': '10-003-1387-0001', 'kor_co_nm': '농협은행주식회사', 'fin_prdt_nm': 'NH고향사랑기부예금'}, {'fin_prdt_cd': '4', 'kor_co_nm': '하나은 행', 'fin_prdt_nm': '하나의정기예금'}, {'fin_prdt_cd': '01013000110000000001', 'kor_co_nm': '주식회사 케이뱅크', 'fin_prdt_nm': '코드K 정기예금'}, {'fin_prdt_cd': '10120110400011', 'kor_co_nm': '수협은행', 'fin_prdt_nm': 'Sh평생주거래우대예금\n(만기일시지급식)'}, {'fin_prdt_cd': '10120114300011', 'kor_co_nm': '수협은행', 'fin_prdt_nm': 'Sh해양플라스틱Zero!예금\n(만기일시지급 식)'}, {'fin_prdt_cd': '10120114700011', 'kor_co_nm': '수협은행', 'fin_prdt_nm': '헤이(Hey)정기예금'}, {'fin_prdt_cd': '10120116100011', 'kor_co_nm': '수협은행', 'fin_prdt_nm': 'Sh첫만남우대예금'}, {'fin_prdt_cd': '10-01-20-388-0002', 'kor_co_nm': '주식회사 카카오뱅크', 'fin_prdt_nm': '카카오뱅크 정기예금'}, {'fin_prdt_cd': '1001202000002', 'kor_co_nm': '토스뱅크 주식회사', 'fin_prdt_nm': '토스뱅크  먼저 이자 받는 정기예금'}]) for _ in range(random.randint(0, 5))]
        
        for item in random_list:

            file["model"] = "accounts.Carts"
            file["pk"] = j + 1
            file["fields"] = {
                'user_id': i+1,
                # 랜덤한 0~5개의 상품을 가입하도록 삽입됨
                'fin_prdt_cd': item['fin_prdt_cd'],
                'kor_co_nm': item['kor_co_nm'],
                'fin_prdt_nm': item['fin_prdt_nm'],
                'created_at': random.choice(["2023-11-23T01:24:17.504Z", "2022-11-24T01:24:15.504Z", "2023-04-20T11:24:17.504Z", "2022-10-13T01:14:17.504Z",
                                             "2022-12-04T01:25:27.504Z", "2023-06-11T06:22:14.504Z", "2023-10-08T05:24:38.504Z", "2022-09-08T09:24:11.504Z"])
            }
            j += 1
            json.dump(file, f, ensure_ascii=False, indent="\t")
            if i != N-1 or random_list[-1] != item:
                f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')