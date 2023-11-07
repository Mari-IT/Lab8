from django.core.management.base import BaseCommand
from mydjangoapp.models import Products

class Command(BaseCommand):
    help = 'Populate Products table with data'

    def handle(self, *args, **options):
        products_data = [
            ('Товар1', 10.99, 100),
            ('Товар2', 19.99, 50),
            ('Товар3', 5.99, 200),
            ('Товар4', 25.99, 75),
            ('Товар5', 7.99, 150),
            ('Товар6', 14.99, 90),
            ('Товар7', 8.49, 120),
            ('Товар8', 12.49, 80),
            ('Товар9', 17.99, 60),
            ('Товар10', 9.99, 110)
        ]

        for data in products_data:
            product = Products(
                Product_Name=data[0],
                Price=data[1],
                Quantity_In_Store=data[2]
            )
            product.save()

        self.stdout.write(self.style.SUCCESS('Successfully filled Products table'))