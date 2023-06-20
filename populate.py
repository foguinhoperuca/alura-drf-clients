import os

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

import random

from faker import Faker
from validate_docbr import CPF

from clients.models import Client


def create_clients(total_clients):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(total_clients):
        cpf_doc = CPF()
        name = fake.name()
        email = '{}@{}'.format(name.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf_doc.generate()
        rg = '{}{}{}{}'.format(random.randrange(10, 99), random.randrange(100, 999), random.randrange(100, 999), random.randrange(0, 9))
        mobile_phone = "({})9{}-{}".format(random.randrange(10, 50), random.randrange(4000, 9999), random.randrange(4000, 9999))
        active = random.choice([True, False])
        cli = Client(name=name, email=email, cpf=cpf, rg=rg, mobile_phone=mobile_phone, active=active)
        cli.save()


if __name__ == '__main__':
    total_clients = random.randint(1, 50)
    create_clients(total_clients)
    print(f"Created {total_clients} clients.")
    
