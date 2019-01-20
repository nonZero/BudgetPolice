from django.urls import path

from expenses.views import expense_list, ExpenseCreateView, expense_detail

app_name = "expenses"

urlpatterns = [
    path('', expense_list, name="list"),
    path('add/', ExpenseCreateView.as_view(), name="create"),
    path('<int:pk>/', expense_detail, name="detail"),
]
