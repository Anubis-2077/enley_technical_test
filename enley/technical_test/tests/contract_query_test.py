from django.test import TestCase
from time import time
from technical_test.tests.factories.contract_factory import UserFactory, ContractFactory, RecurrentContractsFactory
from django.db.models import Subquery
#app imports
from technical_test.models import Contracts, RecurrentContracts


class PerformanceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """probar si los usuarios, contratos y contratos recurrentes se crean correctamente"""
        # Crear 50 usuarios
        for _ in range(50):
            UserFactory()
        print('user_creation_ok')

        # Crear 45 contratos
        for _ in range(45):
            ContractFactory()
        print('contract_creation_ok')

        # Crear 30 contratos recurrentes
        for _ in range(30):
            RecurrentContractsFactory()
        print('recurrent_contracts_creation_ok')
        

    def test_query_performance(self):
        """Probar el rendimiento de las consultas"""
        #ultima medicion Query took 0.00 seconds
        start_time = time()
        try:
            contracts = Contracts.objects.filter(
                start_date__year=2020, user__name__icontains='Jho'
            ).exclude(
                id__in=Subquery(RecurrentContracts.objects.values('contract_id'))
            ).select_related('user').order_by('start_date')
            print('contracts_query_ok')
            for i in contracts:
                print(f"contrato fecha: {i.start_date.strftime('%Y-%m-%d')} usuario: {i.user.name}")
            
        except Exception as e:
            self.fail(f"Query raised an exception: {e}")
        end_time = time()
        elapsed_time = end_time - start_time
        
        print(f"Query took {elapsed_time:.2f} seconds")
        self.assertTrue(contracts.exists(), "No contracts found for the given criteria")