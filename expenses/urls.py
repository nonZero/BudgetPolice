from django.urls import path

from expenses.views import ExpenseCreateView, expense_detail, \
    ExpenseListView

app_name = "expenses"

urlpatterns = [
    path('', ExpenseListView.as_view(), name="list"),
    path('add/', ExpenseCreateView.as_view(), name="create"),
    path('<int:pk>/', expense_detail, name="detail"),
]
