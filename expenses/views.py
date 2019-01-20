from django import forms
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


class ExpenseForm(forms.Form):
    name = forms.CharField(max_length=100)
    amount = forms.DecimalField(decimal_places=2, max_digits=10, required=False)
    are_you_sure = forms.BooleanField()
    flavours = forms.MultipleChoiceField(choices=(
        (1, 'Vanilla'),
        (2, 'Strwberry'),
        (3, 'Chochlate'),
    ))


def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            assert False, form.cleaned_data
    else:
        form = ExpenseForm()

    return render(request, "expenses/expense_form.html", {
        'form': form,
    })
