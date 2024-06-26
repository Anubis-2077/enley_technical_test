from django.core.management.base import BaseCommand
from faker import Faker
from django.utils import timezone
import random
from datetime import datetime
import pytz
from django.db import transaction
#technical_test imports
from technical_test.models import User, Contracts, RecurrentContracts





class Command(BaseCommand):
    help = 'Poblar la base de datos'

    def handle(self, *args, **kwargs):
        fake = Faker()
        try:

            with transaction.atomic():
                self.create_users(fake)
                self.create_contracts(fake)
                self.create_recurrent_contracts()
        except Exception as e:
            print(f"Error al crear los datos {e}")

    def create_users(self, fake):
        usernames = [fake.user_name() for _ in range(50)]
        names = [fake.first_name() for _ in range(80)]
        names.extend(["Jho"] * 10)

        users = [
            User(
                date_joined=fake.date_time_between(start_date='-5y', end_date='-1y'),
                username=random.choice(usernames),
                name=random.choice(names),
                first_name=fake.first_name()
            ) for _ in range(5000000)
        ]

        try:
            User.objects.bulk_create(users, batch_size=1000)
            self.stdout.write(self.style.SUCCESS('5000000 usuarios creados.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creando usuarios: {str(e)}'))

    def create_contracts(self, fake):
        users = list(User.objects.all())

        contracts = [
            Contracts(
                start_date=fake.date_time_between_dates(datetime_start=datetime(2019, 1, 1), datetime_end=datetime(2021, 12, 31)),
                product_id=fake.random_int(min=1, max=100),
                user=random.choice(users)
            ) for _ in range(4000000)
        ]

        try:
            Contracts.objects.bulk_create(contracts, batch_size=1000)
            self.stdout.write(self.style.SUCCESS('4000000 contratos creados.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creando contratos: {str(e)}'))

    def create_recurrent_contracts(self):
        contracts = list(Contracts.objects.all())
        selected_contracts = set()

        while len(selected_contracts) < 3200000:
            contract = random.choice(contracts)
            if contract.id not in selected_contracts:
                selected_contracts.add(contract.id)

        recurrent_contracts_list = [
            RecurrentContracts(
                contract=Contracts.objects.get(id=contract_id)
            ) for contract_id in selected_contracts
        ]

        try:
            RecurrentContracts.objects.bulk_create(recurrent_contracts_list, batch_size=1000)
            self.stdout.write(self.style.SUCCESS('3200000 contratos recurrentes creados.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creando contratos recurrentes: {str(e)}'))
