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
save_dir = 'recommends/fixtures/recommends.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    
    for i in range(N):
        # 랜덤한 데이터를 삽입
        file["model"] = "recommends.AddInfo"
        file["pk"] = i+1
        file["fields"] = {
            'user_id': i+1,
            'target_place': random.choice(['강릉시', '거제시', '경산시']),
            'move_time': random.choice(['2024-10', '2025-02', '2024-12', '2026-04', '2024-02', '2024-06', '2025-10', '2025-09', '2025-03', '2026-06', '2026-11']),
            'deposit_money': (random.randint(1000, 10000)),
            'saving_money': (random.randint(10, 1000)),
            'total_money': (random.randint(8000, 12000)),
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != N-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')