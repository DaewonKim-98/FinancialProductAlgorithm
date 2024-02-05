from django.urls import path
from . import views


urlpatterns = [
    path('save-exchange-data/', views.save_exchange_data),
    path('pull-list/', views.pull_list),
    path('pull-exchanges/', views.pull_exchanges),
]
