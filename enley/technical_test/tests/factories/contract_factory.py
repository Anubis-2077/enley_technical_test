from factory.django import DjangoModelFactory
import factory
from faker import Faker
from technical_test.tests.providers.contract_provider import date_range_provider, name_provider, product_id_provider
import datetime
#internal imports
from technical_test.models import User, Contracts, RecurrentContracts


fake = Faker()
fake.add_provider(date_range_provider)
fake.add_provider(name_provider)
fake.add_provider(product_id_provider)



class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    date_joined = factory.LazyFunction(lambda: fake.date_time_between(start_date='-10y', end_date='now', tzinfo=datetime.timezone.utc))
    username = factory.Faker('user_name')
    name = factory.LazyFunction(lambda: fake.name_custom())
    first_name = factory.Faker('first_name')

class ContractFactory(DjangoModelFactory):
    class Meta:
        model = Contracts

    start_date = factory.LazyFunction(lambda: fake.start_range())
    product_id = factory.LazyFunction(lambda: fake.product_id())
    user = factory.SubFactory(UserFactory)

class RecurrentContractsFactory(DjangoModelFactory):
    class Meta:
        model = RecurrentContracts

    contract = factory.SubFactory(ContractFactory)