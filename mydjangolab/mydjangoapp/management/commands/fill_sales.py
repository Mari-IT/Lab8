from django.core.management.base import BaseCommand
from mydjangoapp.models import Sales
from datetime import date

class Command(BaseCommand):
    help = 'Populate Sales table with data'

    def handle(self, *args, **options):
        sales_data = [
            ('2023-01-01', 1, 2, 5, 10.0, 'готівковий', 0, 0.0),
            ('2023-01-02', 2, 4, 3, 5.0, 'безготівковий', 1, 15.0),
            ('2023-01-03', 1, 1, 2, 7.5, 'готівковий', 0, 0.0),
            ('2023-01-04', 3, 6, 7, 8.0, 'безготівковий', 0, 0.0),
            ('2023-01-05', 4, 3, 4, 12.0, 'готівковий', 1, 25.0),
            ('2023-01-06', 2, 9, 1, 15.0, 'готівковий', 1, 18.0),
            ('2023-01-07', 3, 10, 8, 6.0, 'безготівковий', 0, 0.0),
            ('2023-01-08', 1, 5, 6, 9.0, 'готівковий', 0, 0.0),
            ('2023-01-09', 4, 2, 3, 20.0, 'безготівковий', 1, 22.0),
            ('2023-01-10', 3, 7, 5, 11.0, 'готівковий', 0, 0.0),
            ('2023-01-11', 1, 8, 4, 16.0, 'готівковий', 1, 12.0),
            ('2023-01-12', 2, 1, 3, 14.0, 'безготівковий', 0, 0.0),
            ('2023-01-13', 4, 4, 2, 10.0, 'готівковий', 0, 0.0),
            ('2023-01-14', 2, 6, 5, 7.0, 'безготівковий', 0, 0.0),
            ('2023-01-15', 1, 3, 4, 18.0, 'готівковий', 1, 15.0),
            ('2023-01-16', 3, 9, 2, 10.0, 'готівковий', 0, 0.0),
            ('2023-01-17', 4, 2, 1, 5.0, 'безготівковий', 1, 20.0),
            ('2023-01-18', 2, 5, 3, 12.0, 'готівковий', 0, 0.0),
            ('2023-01-19', 1, 8, 7, 15.0, 'готівковий', 0, 0.0)
        ]

        for data in sales_data:
            sale = Sales(
                Sale_Date=date.fromisoformat(data[0]),
                Customer_ID_id=data[1],
                Product_ID_id=data[2],
                Sold_Quantity=data[3],
                Discount=data[4],
                Payment_Method=data[5],
                Need_Delivery=data[6],
                Delivery_Cost=data[7]
            )
            sale.save()

        self.stdout.write(self.style.SUCCESS('Successfully filled Sales table'))