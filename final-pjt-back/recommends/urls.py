from django.urls import path
from . import views


urlpatterns = [
    path('save-info/', views.save_info),
    path('view-info/', views.view_info),
    path('save-apart/', views.save_apart),
    path('apart/', views.apart),
    path('recommends_products/', views.recommends_products),
    path('products-ranking/', views.products_ranking)
]
