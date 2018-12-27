from django.contrib import admin
from django.urls import path, include

from expenses.views import expense_list

urlpatterns = [
    path('', expense_list),
]
