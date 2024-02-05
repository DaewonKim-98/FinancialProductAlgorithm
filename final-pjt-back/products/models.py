from django.db import models

class DepositProducts(models.Model):
    fin_prdt_cd  = models.TextField(unique=True)           # 금융 상품 코드
    kor_co_nm = models.TextField()                         # 금융회사명
    fin_prdt_nm = models.TextField()                       # 금융 상품명
    etc_note = models.TextField()                          # 금융 상품 설명
    join_deny = models.IntegerField()                      # 가입 제한(1: 제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField()                       # 가입대상
    join_way = models.TextField()                          # 가입 방법
    spcl_cnd = models.TextField()                          # 우대조건


class DepositOptions(models.Model):
    product = models.ForeignKey("DepositProducts", on_delete=models.CASCADE)
    fin_prdt_cd  = models.TextField()                      # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)   # 저축금리 유형명
    intr_rate = models.FloatField()                        # 저축금리
    intr_rate2 = models.FloatField()                       # 최고우대금리
    save_trm = models.IntegerField()                       # 저축기간 (단위: 개월)


class SavingProducts(models.Model):
    fin_prdt_cd  = models.TextField(unique=True)           # 금융 상품 코드
    kor_co_nm = models.TextField()                         # 금융회사명
    fin_prdt_nm = models.TextField()                       # 금융 상품명
    etc_note = models.TextField()                          # 금융 상품 설명
    join_deny = models.IntegerField()                      # 가입 제한(1: 제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField()                       # 가입대상
    join_way = models.TextField()                          # 가입 방법
    spcl_cnd = models.TextField()                          # 우대조건


class SavingOptions(models.Model):
    product = models.ForeignKey("SavingProducts", on_delete=models.CASCADE)
    fin_prdt_cd  = models.TextField()                      # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)   # 저축금리 유형명
    intr_rate = models.FloatField()                        # 저축금리
    intr_rate2 = models.FloatField()                       # 최고우대금리
    save_trm = models.IntegerField()                       # 저축기간 (단위: 개월)


class MortgageLoanProducts(models.Model):
    fin_prdt_cd  = models.TextField(unique=True)           # 금융 상품 코드
    kor_co_nm = models.TextField()                         # 금융회사명
    fin_prdt_nm = models.TextField()                       # 금융 상품명
    loan_inci_expn = models.TextField()                    # 대출 부대비용
    erly_rpay_fee = models.TextField()                     # 중도상환 수수료
    dly_rate = models.TextField()                          # 연체 이자율
    loan_lmt = models.TextField()                          # 대출한도
    join_way = models.TextField()                          # 가입 방법


class MortgageLoanOptions(models.Model):
    product = models.ForeignKey("MortgageLoanProducts", on_delete=models.CASCADE)
    fin_prdt_cd  = models.TextField()                      # 금융 상품 코드
    mrtg_type_nm = models.CharField(max_length=100)        # 담보 유형명
    rpay_type_nm = models.CharField(max_length=100)        # 대출상환 유형명
    lend_rate_type_nm = models.CharField(max_length=100)   # 대출금리 유형명
    lend_rate_min = models.FloatField()                    # 대출금리_최저
    lend_rate_max = models.FloatField()                    # 대출금리_최고
    lend_rate_avg = models.FloatField()                    # 전월 취급 평균금리


class CreditLoanProducts(models.Model):
    fin_prdt_cd  = models.TextField(unique=True)           # 금융 상품 코드
    kor_co_nm = models.TextField()                         # 금융회사명
    fin_prdt_nm = models.TextField()                       # 금융 상품명
    crdt_prdt_type_nm = models.TextField()                 # 대출 종류명
    join_way = models.TextField()                          # 가입 방법


class CreditLoanOptions(models.Model):
    product = models.ForeignKey("CreditLoanProducts", on_delete=models.CASCADE)
    fin_prdt_cd  = models.TextField()                      # 금융 상품 코드
    crdt_lend_rate_type_nm = models.TextField()            # 금리구분
    crdt_grad_1 = models.FloatField()                      # 900점 초과
    crdt_grad_4 = models.FloatField()                      # 801점 ~ 900점
    crdt_grad_5 = models.FloatField()                      # 701점 ~ 800점
    crdt_grad_6 = models.FloatField()                      # 601점 ~ 700점
    crdt_grad_10 = models.FloatField()                     # 501점 ~ 600점
    crdt_grad_11 = models.FloatField()                     # 401점 ~ 500점
    crdt_grad_12 = models.FloatField()                     # 301점 ~ 400점
    crdt_grad_13 = models.FloatField()                     # 300점 이하
    crdt_grad_avg = models.FloatField()                    # 평균 금리