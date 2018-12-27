from django.shortcuts import render

from expenses.models import Expense


def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'x': 123,
        'y': Expense.objects.all(),
    })
