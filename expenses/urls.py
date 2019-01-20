from django.contrib import admin
from django.urls import path, include

from expenses.views import expense_list, expense_detail

app_name = "expenses"

urlpatterns = [
    path('', expense_list, name="list"),
    path('expense/<int:pk>/', expense_detail, name="detail"),
]
