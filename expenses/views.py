from django.http import JsonResponse
from django.shortcuts import render

from expenses.models import Expense


def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.order_by('-date', '-id'),
    })
