from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

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


# class ExpenseForm(forms.ModelForm):
#     class Meta:
#         model = Expense
#         fields = "__all__"
#
#
#
# def expense_create(request):
#     if request.method == "POST":
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             # form.instance.amount = "99.99"
#             form.instance.save()
#             return redirect(form.instance)
#
#
#     else:
#         form = ExpenseForm()
#
#     return render(request, "expenses/expense_form.html", {
#         'form': form,
#     })

class ExpenseCreateView(CreateView):
    model = Expense
    fields = "__all__"
