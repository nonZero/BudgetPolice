from django.test import TestCase

from expenses.models import Expense


class ExpensesTestCase(TestCase):
    def test_simple(self):
        self.assertEqual(Expense.objects.count(), 0)

        o = Expense(
            date="2018-12-13",
            amount="11.23",
            title="Ramen",
            description="Delicious!!!!"
        )
        o.save()

        self.assertEqual(Expense.objects.count(), 1)
