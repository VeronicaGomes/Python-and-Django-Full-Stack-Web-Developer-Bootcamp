import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from appTwo.models import User
from faker import Faker

fake_gen = Faker()


def populate(N = 20):
    for entry in range(N):    
        fake_name = fake_gen.name().split()

        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake_gen.email()

        user = User.objects.get_or_create(first_name = fake_first_name,
                                          last_name = fake_last_name,
                                          email = fake_email)[0]

if __name__ == '__main__':
    print('populate script')
    populate(20)
    print('populate complete')
