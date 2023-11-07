from django.core.management.base import BaseCommand
from mydjangoapp.models import Customers

class Command(BaseCommand):
    help = 'Populate Customers table with data'

    def handle(self, *args, **options):
        customers_data = [
            ('Клієнт1', 'юридична', 'Адреса1', '+1234567890', 'Контактна особа1', 'Рахунок1'),
            ('Клієнт2', 'фізична', 'Адреса2', '+9876543210', 'Контактна особа2', 'Рахунок2'),
            ('Клієнт3', 'юридична', 'Адреса3', '+1112223333', 'Контактна особа3', 'Рахунок3'),
            ('Клієнт4', 'фізична', 'Адреса4', '+4445556666', 'Контактна особа4', 'Рахунок4')
        ]

        for data in customers_data:
            customer = Customers(
                Customer_Name=data[0],
                Legal_or_Natural_Person=data[1],
                Address=data[2],
                Phone=data[3],
                Contact_Person=data[4],
                Bank_Account=data[5]
            )
            customer.save()

        self.stdout.write(self.style.SUCCESS('Successfully filled Customers table'))