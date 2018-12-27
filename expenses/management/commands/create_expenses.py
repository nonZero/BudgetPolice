import silly
from django.core.management.base import BaseCommand

from expenses.models import Expense
import random


class Command(BaseCommand):
    help = "Create some expenses"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):

        Expense.objects.all().delete()

        for i in range(n):
            o = Expense(
                date=f"20{random.randint(15,25)}-{random.randint(1,12):02d}-{random.randint(1,25):02d}",
                title=silly.thing() ,
                amount=f"{random.randint(1, 1000)}.{random.randint(0,99)}",
                description=silly.paragraph(),
            )
            o.save()
