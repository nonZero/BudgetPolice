from django.contrib import admin
from django.urls import path, include

from expenses.views import expense_list, expense_detail, expense_create

app_name = "expenses"

urlpatterns = [
    path('', expense_list, name="list"),
    path('add/', expense_create, name="create"),
    path('<int:pk>/', expense_detail, name="detail"),
]
