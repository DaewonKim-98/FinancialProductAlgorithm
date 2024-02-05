from django.urls import path
from . import views


urlpatterns = [
    # 예금
    path('save-deposit-products/', views.save_deposit_products),
    path('deposit-products/', views.deposit_products),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options),
    # 적금
    path('save-saving-products/', views.save_saving_products),
    path('saving-products/', views.saving_products),
    path('saving-product-options/<str:fin_prdt_cd>/', views.saving_product_options),
    # 저택 담보 대출
    path('save-mortgage-loan-products/', views.save_mortgageloan_products),
    path('mortgage-loan-products/', views.mortgageloan_products),
    path('mortgage-loan-product-options/<str:fin_prdt_cd>/', views.mortgageloan_product_options),
    # 개인 신용 대출
    path('save-credit-loan-products/', views.save_creditloan_products),
    path('credit-loan-products/', views.creditloan_products),
    path('credit-loan-product-options/<str:fin_prdt_cd>/', views.creditloan_product_options),
    # 정기 예금 은행 목록 반환
    path('bank-list/', views.bank_list),
    # 대출 은행 목록 반환
    path('corper-list/', views.corper_list)
]
