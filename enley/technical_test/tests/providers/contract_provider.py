from faker import Faker
from faker.providers import DynamicProvider
import datetime



fake= Faker()



date_range_provider = DynamicProvider(
    provider_name="start_range",
    elements = [
    datetime.datetime(2019, 12, 15),
    datetime.datetime(2020, 1, 10),
    datetime.datetime(2020, 6, 20),
    datetime.datetime(2020, 11, 5),
    datetime.datetime(2021, 2, 17),
    datetime.datetime(2021, 8, 22),
    datetime.datetime(2022, 1, 30),
    datetime.datetime(2022, 5, 25),
    datetime.datetime(2023, 3, 14),
    datetime.datetime(2023, 7, 9),
]
)

product_id_provider = DynamicProvider(
    provider_name="product_id",
    elements=[i for i in range(1, 100)]
)


name_provider = DynamicProvider(
    provider_name='name_custom',
    elements=
            [
            'John',
            'Jane',
            'Bob',
            'Alice',
            'Mike',
            'Jhonson',
            'Jho'
            'Jhoanna'
        ]
    )