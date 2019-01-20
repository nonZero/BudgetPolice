from django import forms
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, FormView, ListView

from expenses.models import Expense


class ExpenseListView(ListView):
    model = Expense
    ordering = ("-date", "-id")
    # paginate_by = 10

# def expense_list(request):
#     return render(request, "expenses/expense_list.html", {
#         'object_list': Expense.objects.order_by('-date', '-id'),
#     })


def expense_detail(request, pk):
    o = get_object_or_404(Expense, pk=pk)

    return render(request, "expenses/expense_detail.html", {
        'object': o,
    })


class ExpenseCreateView(CreateView):
    model = Expense
    fields = "__all__"


class MyForm(forms.Form):
    are_you_sure = forms.BooleanField()


class MyFormView(FormView):
    form_class = MyForm

    def form_valid(self, form):
        assert False, form.cleaned_data
