from django.shortcuts import render, get_object_or_404

from expenses.models import Expense


def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.order_by('-date', '-id'),
    })


def expense_detail(request, pk):
    o = get_object_or_404(Expense, pk=pk)

    return render(request, "expenses/expense_detail.html", {
        'object': o,
    })


def expense_create(request):
    if request.method == "POST":
        assert False, request.POST
    return render(request, "expenses/expense_form.html", {
    })
