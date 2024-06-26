from django.urls import path
from technical_test.views import ContractListView


urlpatterns = [
    path('contract_list/', ContractListView.as_view(), name='contract_list')
]
